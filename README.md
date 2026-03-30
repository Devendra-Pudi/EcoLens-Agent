# ♻️ EcoLens - The Intelligent Waste Analyst

A Multimodal Multi-Agent System for Smart Waste Management powered by Google Gemini AI.

## 🌟 Features

- **AI-Powered Analysis**: Three specialized agents analyze waste items
  - 🔬 Wall-E: Material Scientist (identifies materials and condition)
  - 👮 Eve: Compliance Officer (determines proper disposal method)
  - 🎨 MacGyver: Upcycling Expert (suggests creative reuse ideas)
- **Modern UI**: React + Vite + Tailwind CSS
- **Fast API Backend**: Python FastAPI with rate limiting
- **Image Upload**: Drag-and-drop or click to upload
- **Export Reports**: Download analysis as Markdown

## 🚀 Tech Stack

### Frontend
- React 18
- Vite
- Tailwind CSS

### Backend
- FastAPI
- Google Gemini 2.5 Flash
- SlowAPI (rate limiting)
- Python 3.10+

## 📦 Installation

### Prerequisites
- Python 3.10+
- Node.js 18+
- Google API Key ([Get one here](https://aistudio.google.com/app/apikey))

### Backend Setup

```bash
cd fastapi-app
pip install -r requirements.txt
```

Create `.env` file in the root directory:
```
GOOGLE_API_KEY=your_api_key_here
```

Run the backend:
```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Visit http://localhost:3000

## 🌐 Deployment

### Vercel Deployment

1. Fork this repository
2. Import to Vercel
3. Add environment variable: `GOOGLE_API_KEY`
4. Deploy!

The app will automatically deploy both frontend and backend.

## 📝 API Endpoints

- `GET /health` - Health check
- `POST /api/analyze` - Analyze waste item (5/min, 20/hour)
- `GET /api/results/{id}` - Get analysis results
- `GET /api/history` - Get analysis history
- `GET /api/export/{id}` - Export report (json/markdown/txt)
- `GET /docs` - API documentation

## 🎯 Rate Limits

- `/api/analyze`: 5 requests/minute, 20 requests/hour
- `/health`: 60 requests/minute
- Other endpoints: 30 requests/minute

## 📄 License

MIT License

## 👥 Authors

Devendra Pudi

## 🙏 Acknowledgments

- Google Gemini AI
- FastAPI
- React + Vite
