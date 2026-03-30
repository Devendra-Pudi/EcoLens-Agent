@echo off
REM EcoLens Quick Start Script for Windows

echo ==================================================
echo ♻️  EcoLens - Quick Start Setup
echo ==================================================
echo.

REM Check Python
echo 🔍 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% found
echo.

REM Install dependencies
echo 📦 Installing dependencies...
pip install -q -r requirements_web.txt
echo ✅ Dependencies installed
echo.

REM Check API key
echo 🔑 Checking API key...
if "%GOOGLE_API_KEY%"=="" (
    echo ⚠️  GOOGLE_API_KEY not set
    echo.
    echo Get a free API key at: https://aistudio.google.com/apikey
    echo.
    set /p API_KEY="Enter your Gemini API key: "
    
    if "%API_KEY%"=="" (
        echo ❌ No API key provided. Exiting.
        pause
        exit /b 1
    )
    
    set GOOGLE_API_KEY=%API_KEY%
    echo ✅ API key set for this session
) else (
    echo ✅ API key found
)
echo.

REM Choose what to run
echo What would you like to run?
echo 1) Streamlit Frontend (Recommended for users)
echo 2) FastAPI Backend (For developers)
echo 3) Both (Full system)
echo 4) Demo Simulation (No API key needed)
echo.
set /p CHOICE="Enter your choice (1-4): "

if "%CHOICE%"=="1" (
    echo.
    echo 🚀 Starting Streamlit Frontend...
    echo    Opening http://localhost:8501
    echo.
    streamlit run app_streamlit.py
) else if "%CHOICE%"=="2" (
    echo.
    echo 🚀 Starting FastAPI Backend...
    echo    API available at http://localhost:8000
    echo    Docs at http://localhost:8000/docs
    echo.
    python app_fastapi.py
) else if "%CHOICE%"=="3" (
    echo.
    echo 🚀 Starting both services...
    echo    Frontend: http://localhost:8501
    echo    API: http://localhost:8000
    echo    Docs: http://localhost:8000/docs
    echo.
    echo Starting FastAPI in background...
    start python app_fastapi.py
    
    timeout /t 2 /nobreak
    
    echo Starting Streamlit...
    streamlit run app_streamlit.py
) else if "%CHOICE%"=="4" (
    echo.
    echo 🎬 Running Demo Simulation...
    echo    (No API key needed)
    echo.
    python demo_simulation.py
) else (
    echo ❌ Invalid choice
    pause
    exit /b 1
)

pause
