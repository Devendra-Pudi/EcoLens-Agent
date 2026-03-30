#!/bin/bash

# EcoLens Quick Start Script
# This script helps you set up and run EcoLens

set -e

echo "=================================================="
echo "♻️  EcoLens - Quick Start Setup"
echo "=================================================="
echo ""

# Check Python
echo "🔍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $PYTHON_VERSION found"
echo ""

# Check pip
echo "🔍 Checking pip installation..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip not found. Please install pip."
    exit 1
fi
echo "✅ pip found"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -q -r requirements_web.txt
echo "✅ Dependencies installed"
echo ""

# Check API key
echo "🔑 Checking API key..."
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️  GOOGLE_API_KEY not set"
    echo ""
    echo "Get a free API key at: https://aistudio.google.com/apikey"
    echo ""
    read -p "Enter your Gemini API key: " API_KEY
    
    if [ -z "$API_KEY" ]; then
        echo "❌ No API key provided. Exiting."
        exit 1
    fi
    
    export GOOGLE_API_KEY="$API_KEY"
    echo "✅ API key set for this session"
else
    echo "✅ API key found"
fi
echo ""

# Choose what to run
echo "What would you like to run?"
echo "1) Streamlit Frontend (Recommended for users)"
echo "2) FastAPI Backend (For developers)"
echo "3) Both (Full system)"
echo "4) Demo Simulation (No API key needed)"
echo ""
read -p "Enter your choice (1-4): " CHOICE

case $CHOICE in
    1)
        echo ""
        echo "🚀 Starting Streamlit Frontend..."
        echo "   Opening http://localhost:8501"
        echo ""
        streamlit run app_streamlit.py
        ;;
    2)
        echo ""
        echo "🚀 Starting FastAPI Backend..."
        echo "   API available at http://localhost:8000"
        echo "   Docs at http://localhost:8000/docs"
        echo ""
        python3 app_fastapi.py
        ;;
    3)
        echo ""
        echo "🚀 Starting both services..."
        echo "   Frontend: http://localhost:8501"
        echo "   API: http://localhost:8000"
        echo "   Docs: http://localhost:8000/docs"
        echo ""
        echo "Starting FastAPI in background..."
        python3 app_fastapi.py &
        API_PID=$!
        
        sleep 2
        
        echo "Starting Streamlit..."
        streamlit run app_streamlit.py
        
        # Cleanup on exit
        trap "kill $API_PID" EXIT
        ;;
    4)
        echo ""
        echo "🎬 Running Demo Simulation..."
        echo "   (No API key needed)"
        echo ""
        python3 demo_simulation.py
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac
