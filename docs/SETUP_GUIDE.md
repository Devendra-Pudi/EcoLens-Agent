# EcoLens Setup Guide

Complete guide to set up and run EcoLens with Streamlit frontend and FastAPI backend.

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

## 🚀 Quick Start

### 1. Get Your API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API Key"
3. Copy your API key

### 2. Set Environment Variable

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY = "AIzaSyBh7GI4eBTxek3tC92pwQ2yLrDd_xDTiDk"
```

**Windows (Command Prompt):**
```cmd
set GOOGLE_API_KEY=AIzaSyBh7GI4eBTxek3tC92pwQ2yLrDd_xDTiDk
```

**Linux/Mac:**
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

### 3. Install Dependencies

```bash
pip install -r requirements_web.txt
```

## 🎨 Option 1: Streamlit Frontend (Recommended for Users)

Streamlit provides a beautiful, interactive web interface.

### Start the Streamlit App

```bash
streamlit run app_streamlit.py
```

The app will open in your browser at `http://localhost:8501`

### Features

- 📸 Upload waste item photos
- 🔬 Get material analysis from Wall-E
- 👮 Get disposal verdict from Eve
- 🎨 Get upcycling ideas from MacGyver
- 📚 Learn about waste management
- 📥 Download analysis reports
- ❓ FAQ and tips

### Usage

1. Set your API key in the sidebar
2. Upload an image of a waste item
3. Click "Analyze with EcoLens"
4. View results from all three agents
5. Download the report if needed

## 🔌 Option 2: FastAPI Backend (For Developers)

FastAPI provides a RESTful API with automatic documentation.

### Start the FastAPI Server

```bash
python app_fastapi.py
```

Or with uvicorn directly:

```bash
uvicorn app_fastapi:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API Endpoints

#### Health & Info
- `GET /` - API information
- `GET /health` - Health check
- `GET /info` - Detailed API info
- `GET /api/agents` - Agent information
- `GET /api/materials` - Material information
- `GET /api/tips` - Recycling tips

#### Analysis
- `POST /api/analyze` - Analyze waste item (upload image)
- `GET /api/results/{analysis_id}` - Get analysis results
- `GET /api/history` - Get recent analyses
- `DELETE /api/results/{analysis_id}` - Delete result
- `DELETE /api/history` - Clear all history

#### Export
- `GET /api/export/{analysis_id}?format=json` - Export as JSON
- `GET /api/export/{analysis_id}?format=markdown` - Export as Markdown
- `GET /api/export/{analysis_id}?format=txt` - Export as text

### Example API Usage

**Python:**
```python
import requests

# Analyze an image
with open("waste_item.jpg", "rb") as f:
    files = {"file": f}
    response = requests.post("http://localhost:8000/api/analyze", files=files)
    result = response.json()
    print(result)
```

**cURL:**
```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -F "file=@waste_item.jpg"
```

**JavaScript/Fetch:**
```javascript
const formData = new FormData();
formData.append("file", imageFile);

const response = await fetch("http://localhost:8000/api/analyze", {
  method: "POST",
  body: formData
});

const result = await response.json();
console.log(result);
```

## 🌐 Option 3: Run Both Simultaneously

You can run both Streamlit and FastAPI at the same time for a complete system.

### Terminal 1 - Start FastAPI Backend
```bash
python app_fastapi.py
```

### Terminal 2 - Start Streamlit Frontend
```bash
streamlit run app_streamlit.py
```

Now you have:
- Frontend: http://localhost:8501
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 🐳 Docker Setup (Optional)

### Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements_web.txt .
RUN pip install -r requirements_web.txt

COPY . .

ENV GOOGLE_API_KEY=""

EXPOSE 8000 8501

CMD ["sh", "-c", "python app_fastapi.py & streamlit run app_streamlit.py"]
```

### Build and Run

```bash
# Build image
docker build -t ecolens .

# Run container
docker run -e GOOGLE_API_KEY="your_key_here" -p 8000:8000 -p 8501:8501 ecolens
```

## 🧪 Testing

### Test Streamlit App

1. Open http://localhost:8501
2. Set API key in sidebar
3. Upload a test image
4. Click "Analyze with EcoLens"
5. Verify results appear

### Test FastAPI

1. Open http://localhost:8000/docs
2. Click "Try it out" on `/api/analyze`
3. Upload an image
4. Click "Execute"
5. Verify response

## 🔧 Troubleshooting

### "API key not valid"
- Verify your API key is correct
- Check it's set in environment: `echo $GOOGLE_API_KEY`
- Get a new key from https://aistudio.google.com/apikey

### "Module not found"
- Install dependencies: `pip install -r requirements_web.txt`
- Verify Python version: `python --version` (should be 3.8+)

### "Port already in use"
- Streamlit: `streamlit run app_streamlit.py --server.port 8502`
- FastAPI: `uvicorn app_fastapi:app --port 8001`

### "Image upload fails"
- Check file size (should be < 20MB)
- Verify file format (jpg, jpeg, png, gif)
- Check internet connection

### "Analysis takes too long"
- First analysis may take longer (model loading)
- Subsequent analyses are faster
- Check internet connection
- Verify API key is valid

## 📊 Performance Tips

1. **Optimize Images**: Resize large images before uploading
2. **Batch Processing**: Use FastAPI for multiple analyses
3. **Caching**: Results are cached in memory
4. **Local Deployment**: Run on same machine for best performance

## 🔒 Security Considerations

1. **API Key**: Never commit API key to version control
2. **Environment Variables**: Use `.env` file locally
3. **HTTPS**: Use HTTPS in production
4. **Rate Limiting**: Implement in production
5. **Authentication**: Add user authentication for production

### Create .env File (Local Development)

```
GOOGLE_API_KEY=your_api_key_here
```

Then load it:

```python
from dotenv import load_dotenv
load_dotenv()
```

## 📈 Scaling for Production

### Recommendations

1. **Database**: Replace in-memory storage with PostgreSQL/MongoDB
2. **Authentication**: Add user authentication (JWT, OAuth)
3. **Rate Limiting**: Implement rate limiting per user
4. **Caching**: Use Redis for result caching
5. **Monitoring**: Add logging and monitoring
6. **Load Balancing**: Use Nginx/HAProxy for multiple instances
7. **CDN**: Serve static files from CDN
8. **SSL/TLS**: Use HTTPS with valid certificates

### Example Production Stack

```
┌─────────────────┐
│   Nginx (SSL)   │
└────────┬────────┘
         │
    ┌────┴────┐
    │          │
┌───▼──┐  ┌───▼──┐
│ API  │  │ Web  │
│ 8000 │  │ 8501 │
└───┬──┘  └───┬──┘
    │         │
    └────┬────┘
         │
    ┌────▼────────┐
    │  PostgreSQL  │
    │   + Redis    │
    └─────────────┘
```

## 📚 Additional Resources

- [Streamlit Docs](https://docs.streamlit.io/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Google Gemini API](https://ai.google.dev/)
- [Python Requests](https://requests.readthedocs.io/)

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Check API key is valid
4. Review error messages carefully
5. Check internet connection

## 📝 License

MIT License - Feel free to use for good!

---

**Happy analyzing! ♻️**
