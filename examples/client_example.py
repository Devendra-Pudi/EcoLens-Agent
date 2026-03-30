"""
EcoLens API Client Example
Shows how to use the FastAPI backend programmatically
"""

import requests
import json
from pathlib import Path
import time

class EcoLensClient:
    """Client for interacting with EcoLens API"""
    
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def health_check(self):
        """Check if API is healthy"""
        try:
            response = self.session.get(f"{self.base_url}/health")
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def analyze_image(self, image_path):
        """Analyze a waste item from an image file"""
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Image not found: {image_path}")
        
        with open(image_path, "rb") as f:
            files = {"file": f}
            response = self.session.post(
                f"{self.base_url}/api/analyze",
                files=files
            )
        
        if response.status_code != 200:
            raise Exception(f"Analysis failed: {response.text}")
        
        return response.json()
    
    def get_results(self, analysis_id):
        """Get analysis results by ID"""
        response = self.session.get(f"{self.base_url}/api/results/{analysis_id}")
        
        if response.status_code != 200:
            raise Exception(f"Failed to get results: {response.text}")
        
        return response.json()
    
    def get_history(self, limit=10):
        """Get recent analysis history"""
        response = self.session.get(
            f"{self.base_url}/api/history",
            params={"limit": limit}
        )
        
        if response.status_code != 200:
            raise Exception(f"Failed to get history: {response.text}")
        
        return response.json()
    
    def export_report(self, analysis_id, format="markdown"):
        """Export analysis report"""
        response = self.session.get(
            f"{self.base_url}/api/export/{analysis_id}",
            params={"format": format}
        )
        
        if response.status_code != 200:
            raise Exception(f"Failed to export: {response.text}")
        
        return response.json()
    
    def get_agents(self):
        """Get information about all agents"""
        response = self.session.get(f"{self.base_url}/api/agents")
        return response.json()
    
    def get_materials(self):
        """Get information about materials"""
        response = self.session.get(f"{self.base_url}/api/materials")
        return response.json()
    
    def get_tips(self):
        """Get recycling tips"""
        response = self.session.get(f"{self.base_url}/api/tips")
        return response.json()
    
    def delete_result(self, analysis_id):
        """Delete an analysis result"""
        response = self.session.delete(f"{self.base_url}/api/results/{analysis_id}")
        
        if response.status_code != 200:
            raise Exception(f"Failed to delete: {response.text}")
        
        return response.json()
    
    def clear_history(self):
        """Clear all analysis history"""
        response = self.session.delete(f"{self.base_url}/api/history")
        
        if response.status_code != 200:
            raise Exception(f"Failed to clear history: {response.text}")
        
        return response.json()


def main():
    """Example usage of EcoLens client"""
    
    print("=" * 60)
    print("EcoLens API Client Example")
    print("=" * 60)
    
    # Initialize client
    client = EcoLensClient()
    
    # Check health
    print("\n1️⃣ Checking API health...")
    health = client.health_check()
    print(f"   Status: {health.get('status', 'unknown')}")
    print(f"   API Configured: {health.get('api_configured', False)}")
    
    if not health.get('api_configured'):
        print("\n❌ API not configured. Please set GOOGLE_API_KEY environment variable")
        return
    
    # Get agents info
    print("\n2️⃣ Getting agent information...")
    agents = client.get_agents()
    for agent in agents['agents']:
        print(f"   - {agent['name']} ({agent['role']})")
    
    # Get materials info
    print("\n3️⃣ Getting material information...")
    materials = client.get_materials()
    print(f"   Available materials: {', '.join(materials['materials'].keys())}")
    
    # Get tips
    print("\n4️⃣ Getting recycling tips...")
    tips = client.get_tips()
    print(f"   Recycling tips: {len(tips['tips']['recycling'])} tips")
    print(f"   Composting tips: {len(tips['tips']['composting'])} tips")
    print(f"   Upcycling tips: {len(tips['tips']['upcycling'])} tips")
    
    # Analyze image (if available)
    print("\n5️⃣ Analyzing image...")
    
    # Check if test image exists
    if Path("test_trash.jpg").exists():
        print("   Uploading test_trash.jpg...")
        
        try:
            result = client.analyze_image("test_trash.jpg")
            analysis_id = result['analysis_id']
            
            print(f"   ✅ Analysis complete!")
            print(f"   Analysis ID: {analysis_id}")
            print(f"   Status: {result['status']}")
            print(f"   Timestamp: {result['timestamp']}")
            
            # Display results
            print("\n   📊 Results:")
            print(f"\n   🔬 Material Analysis:")
            print(f"   {result['material_analysis'][:200]}...")
            
            print(f"\n   👮 Disposal Verdict:")
            print(f"   {result['verdict'][:200]}...")
            
            print(f"\n   🎨 Upcycling Ideas:")
            print(f"   {result['upcycling_ideas'][:200]}...")
            
            # Export report
            print("\n6️⃣ Exporting report...")
            report = client.export_report(analysis_id, format="markdown")
            print(f"   ✅ Report exported as markdown")
            print(f"   Content length: {len(report['content'])} characters")
            
            # Get history
            print("\n7️⃣ Getting analysis history...")
            history = client.get_history(limit=5)
            print(f"   Total analyses: {history['total']}")
            print(f"   Recent analyses: {history['returned']}")
            
            for analysis in history['analyses']:
                print(f"   - {analysis['analysis_id']}: {analysis['timestamp']}")
        
        except Exception as e:
            print(f"   ❌ Error: {e}")
    else:
        print("   ⚠️ test_trash.jpg not found. Skipping image analysis.")
        print("   To test, download a sample image first:")
        print("   python demo.py")
    
    print("\n" + "=" * 60)
    print("✅ Example complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
