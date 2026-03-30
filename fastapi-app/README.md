# EcoLens FastAPI App

RESTful API with HTML frontend for EcoLens waste analysis.

## Features

- 🌐 HTML/CSS/JS frontend
- 🔌 REST API with 10+ endpoints
- 📚 Auto-generated documentation (Swagger UI, ReDoc)
- 🎨 Beautiful responsive design
- 📊 JSON/Markdown/Text export

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export GOOGLE_API_KEY="your_key_here"

# Run app
python app.py
```

Or with uvicorn:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## Access

- **Frontend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

- `GET /` - HTML frontend
- `GET /health` - Health check
- `POST /api/analyze` - Analyze waste item
- `GET /api/results/{id}` - Get results
- `GET /api/history` - Get history
- `GET /api/export/{id}` - Export report
- `GET /api/agents` - Agent information
- `GET /api/materials` - Material database
- `GET /api/tips` - Recycling tips

## Environment Variables

- `GOOGLE_API_KEY` - Required: Your Gemini API key

## Project Structure

```
fastapi-app/
├── app.py              # Main application
├── templates/          # HTML templates
│   └── index.html
├── static/             # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── requirements.txt    # Dependencies
```
