"""
EcoLens FastAPI Backend
RESTful API for the intelligent waste analyst
"""

from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
import sys
import tempfile
import uuid
from datetime import datetime
import json
from pathlib import Path
from dotenv import load_dotenv
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Load environment variables from .env file
load_dotenv()

# Rate limiter — keyed by client IP
limiter = Limiter(key_func=get_remote_address)

# Add parent directory to path to import ecolens
sys.path.insert(0, str(Path(__file__).parent.parent))
from core.ecolens import configure_api, run_ecolens_pipeline

# Initialize FastAPI app
app = FastAPI(
    title="EcoLens API",
    description="Multimodal Multi-Agent System for Intelligent Waste Analysis",
    version="1.0.0"
)

# Attach rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Add CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://*.vercel.app",
        "https://ecolens-agent.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class AnalysisRequest(BaseModel):
    """Request model for analysis"""
    image_url: Optional[str] = None
    description: Optional[str] = None

class AnalysisResponse(BaseModel):
    """Response model for analysis"""
    analysis_id: str
    material_analysis: str
    verdict: str
    upcycling_ideas: str
    timestamp: str
    status: str

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    api_configured: bool
    version: str

# Storage for analysis results (in-memory, use database for production)
analysis_storage = {}

# ============================================================
# HEALTH & INFO ENDPOINTS
# ============================================================

@app.get("/", tags=["Info"])
@limiter.limit("30/minute")
async def root(request: Request):
    """API root endpoint"""
    return {
        "name": "EcoLens API",
        "version": "1.0.0",
        "status": "running",
        "frontend": "http://localhost:3000",
        "docs": "/docs"
    }

@app.get("/health", response_model=HealthResponse, tags=["Info"])
@limiter.limit("60/minute")
async def health_check(request: Request):
    """Health check endpoint"""
    api_key = os.environ.get("GOOGLE_API_KEY")
    return HealthResponse(
        status="healthy",
        api_configured=bool(api_key),
        version="1.0.0"
    )

@app.get("/info", tags=["Info"])
async def get_info():
    """Get API information"""
    return {
        "name": "EcoLens - The Intelligent Waste Analyst",
        "description": "A Multimodal Multi-Agent System for Smart Waste Management",
        "agents": {
            "wall_e": {
                "name": "Wall-E",
                "role": "Material Scientist",
                "description": "Analyzes waste items using computer vision"
            },
            "eve": {
                "name": "Eve",
                "role": "Compliance Officer",
                "description": "Determines proper disposal method based on rules"
            },
            "macgyver": {
                "name": "MacGyver",
                "role": "Upcycling Expert",
                "description": "Suggests creative reuse ideas"
            }
        },
        "endpoints": {
            "analyze": "/api/analyze",
            "history": "/api/history",
            "results": "/api/results/{analysis_id}"
        }
    }

# ============================================================
# ANALYSIS ENDPOINTS
# ============================================================

@app.post("/api/analyze", response_model=AnalysisResponse, tags=["Analysis"])
@limiter.limit("5/minute;20/hour")
async def analyze_waste(request: Request, file: UploadFile = File(...)):
    """
    Analyze a waste item from an uploaded image
    
    - **file**: Image file (jpg, jpeg, png, gif)
    
    Returns analysis results from all three agents
    """
    
    # Check API key
    if not os.environ.get("GOOGLE_API_KEY"):
        raise HTTPException(
            status_code=503,
            detail="API key not configured. Please set GOOGLE_API_KEY environment variable."
        )
    
    # Validate file type
    allowed_types = ["image/jpeg", "image/png", "image/gif"]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed: {', '.join(allowed_types)}"
        )
    
    try:
        # Generate unique analysis ID
        analysis_id = str(uuid.uuid4())
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            content = await file.read()
            tmp_file.write(content)
            tmp_path = tmp_file.name
        
        # Configure API
        configure_api()
        
        # Run analysis
        results = run_ecolens_pipeline(tmp_path)
        
        # Clean up temp file
        os.unlink(tmp_path)
        
        # Store results
        response = AnalysisResponse(
            analysis_id=analysis_id,
            material_analysis=results["material_analysis"],
            verdict=results["verdict"],
            upcycling_ideas=results["upcycling_ideas"],
            timestamp=datetime.now().isoformat(),
            status="completed"
        )
        
        analysis_storage[analysis_id] = response.dict()
        
        return response
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )

@app.get("/api/results/{analysis_id}", response_model=AnalysisResponse, tags=["Analysis"])
async def get_results(analysis_id: str):
    """
    Get analysis results by ID
    
    - **analysis_id**: The unique analysis identifier
    """
    
    if analysis_id not in analysis_storage:
        raise HTTPException(
            status_code=404,
            detail=f"Analysis with ID {analysis_id} not found"
        )
    
    return AnalysisResponse(**analysis_storage[analysis_id])

@app.get("/api/history", tags=["Analysis"])
@limiter.limit("30/minute")
async def get_history(request: Request, limit: int = 10):
    """
    Get recent analysis history
    
    - **limit**: Maximum number of results to return (default: 10)
    """
    
    # Get most recent analyses
    recent = sorted(
        analysis_storage.items(),
        key=lambda x: x[1]["timestamp"],
        reverse=True
    )[:limit]
    
    return {
        "total": len(analysis_storage),
        "returned": len(recent),
        "analyses": [
            {
                "analysis_id": aid,
                "timestamp": data["timestamp"],
                "status": data["status"]
            }
            for aid, data in recent
        ]
    }

# ============================================================
# EXPORT ENDPOINTS
# ============================================================

@app.get("/api/export/{analysis_id}", tags=["Export"])
async def export_report(analysis_id: str, format: str = "json"):
    """
    Export analysis report in different formats
    
    - **analysis_id**: The unique analysis identifier
    - **format**: Export format (json, markdown, txt)
    """
    
    if analysis_id not in analysis_storage:
        raise HTTPException(
            status_code=404,
            detail=f"Analysis with ID {analysis_id} not found"
        )
    
    data = analysis_storage[analysis_id]
    
    if format == "json":
        return JSONResponse(content=data)
    
    elif format == "markdown":
        content = f"""# EcoLens Analysis Report

**Analysis ID:** {analysis_id}  
**Timestamp:** {data['timestamp']}  
**Status:** {data['status']}

## 🔬 Material Analysis

{data['material_analysis']}

## 👮 Disposal Verdict

{data['verdict']}

## 🎨 Upcycling Ideas

{data['upcycling_ideas']}

---
*Generated by EcoLens - The Intelligent Waste Analyst*
"""
        return JSONResponse(
            content={"content": content, "format": "markdown"},
            media_type="application/json"
        )
    
    elif format == "txt":
        content = f"""EcoLens Analysis Report
{'='*60}

Analysis ID: {analysis_id}
Timestamp: {data['timestamp']}
Status: {data['status']}

MATERIAL ANALYSIS
{'-'*60}
{data['material_analysis']}

DISPOSAL VERDICT
{'-'*60}
{data['verdict']}

UPCYCLING IDEAS
{'-'*60}
{data['upcycling_ideas']}

{'='*60}
Generated by EcoLens - The Intelligent Waste Analyst
"""
        return JSONResponse(
            content={"content": content, "format": "txt"},
            media_type="application/json"
        )
    
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported format: {format}. Supported: json, markdown, txt"
        )

# ============================================================
# UTILITY ENDPOINTS
# ============================================================

@app.get("/api/agents", tags=["Info"])
async def get_agents():
    """Get information about all agents"""
    return {
        "agents": [
            {
                "id": "wall_e",
                "name": "Wall-E",
                "role": "Material Scientist",
                "description": "Analyzes waste items using computer vision",
                "capabilities": [
                    "Material identification",
                    "Condition assessment",
                    "Composition analysis",
                    "Contamination detection"
                ]
            },
            {
                "id": "eve",
                "name": "Eve",
                "role": "Compliance Officer",
                "description": "Determines proper disposal method",
                "capabilities": [
                    "Recycling rule application",
                    "Disposal method determination",
                    "Contamination prevention",
                    "Local guideline compliance"
                ]
            },
            {
                "id": "macgyver",
                "name": "MacGyver",
                "role": "Upcycling Expert",
                "description": "Suggests creative reuse ideas",
                "capabilities": [
                    "DIY project suggestions",
                    "Lifecycle extension",
                    "Creative reuse ideas",
                    "Environmental impact calculation"
                ]
            }
        ]
    }

@app.get("/api/materials", tags=["Info"])
async def get_materials():
    """Get information about common materials"""
    return {
        "materials": {
            "plastic": {
                "types": ["PET (#1)", "HDPE (#2)", "PVC (#3)", "LDPE (#4)", "PP (#5)", "PS (#6)", "Other (#7)"],
                "recyclable": ["#1", "#2", "#5"],
                "tips": "Check resin code, rinse before recycling, remove caps"
            },
            "cardboard": {
                "types": ["Corrugated", "Paperboard", "Kraft"],
                "recyclable": ["Clean cardboard"],
                "tips": "Remove food residue, flatten to save space, separate greasy parts"
            },
            "glass": {
                "types": ["Clear", "Brown", "Green"],
                "recyclable": ["All colors"],
                "tips": "Rinse well, remove metal lids, handle carefully"
            },
            "metal": {
                "types": ["Aluminum", "Steel", "Tin"],
                "recyclable": ["All types"],
                "tips": "Rinse, crush to save space, remove labels"
            },
            "electronics": {
                "types": ["Phones", "Computers", "Appliances"],
                "recyclable": ["All types"],
                "tips": "Find local e-waste facility, data security important"
            }
        }
    }

@app.get("/api/tips", tags=["Info"])
async def get_tips():
    """Get recycling and waste management tips"""
    return {
        "tips": {
            "recycling": [
                "Always rinse containers before recycling",
                "Remove plastic bags - they jam sorting machines",
                "Don't crush aluminum cans - helps sorting",
                "Keep food-soiled items out of recycling",
                "Check local guidelines - rules vary by location"
            ],
            "composting": [
                "Mix green (nitrogen) and brown (carbon) materials",
                "Keep compost moist like a wrung-out sponge",
                "Turn pile regularly for faster decomposition",
                "Avoid meat, dairy, and oils",
                "Use finished compost in gardens"
            ],
            "upcycling": [
                "Think creatively about item uses",
                "Plastic bottles make great planters",
                "Cardboard boxes become organizers",
                "Glass jars work as storage containers",
                "Old clothes become cleaning rags"
            ]
        }
    }

@app.delete("/api/results/{analysis_id}", tags=["Analysis"])
async def delete_result(analysis_id: str):
    """
    Delete an analysis result
    
    - **analysis_id**: The unique analysis identifier
    """
    
    if analysis_id not in analysis_storage:
        raise HTTPException(
            status_code=404,
            detail=f"Analysis with ID {analysis_id} not found"
        )
    
    del analysis_storage[analysis_id]
    
    return {
        "status": "deleted",
        "analysis_id": analysis_id
    }

@app.delete("/api/history", tags=["Analysis"])
async def clear_history():
    """Clear all analysis history"""
    count = len(analysis_storage)
    analysis_storage.clear()
    
    return {
        "status": "cleared",
        "deleted_count": count
    }

# ============================================================
# ERROR HANDLERS
# ============================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code
        }
    )

# ============================================================
# STARTUP & SHUTDOWN
# ============================================================

@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    print("🚀 EcoLens API Starting...")
    
    # Check API key
    if not os.environ.get("GOOGLE_API_KEY"):
        print("⚠️  Warning: GOOGLE_API_KEY not set. Analysis will fail.")
        print("   Set it with: export GOOGLE_API_KEY='your_key_here'")
    else:
        print("✅ API Key configured")
    
    print("✅ EcoLens API Ready!")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    print("👋 EcoLens API Shutting down...")

if __name__ == "__main__":
    import uvicorn
    
    # Check for API key
    if not os.environ.get("GOOGLE_API_KEY"):
        print("⚠️  Please set GOOGLE_API_KEY environment variable")
        print("   export GOOGLE_API_KEY='your_key_here'")
    
    # Run server
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_level="info"
    )
