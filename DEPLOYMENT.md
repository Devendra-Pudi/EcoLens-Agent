# 🚀 Deployment Guide

## Vercel Deployment (Recommended)

### Step 1: Prepare Your Repository
✅ Already done! Your code is pushed to GitHub.

### Step 2: Import to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New" → "Project"
3. Import your GitHub repository: `Devendra-Pudi/EcoLens-Agent`
4. Vercel will auto-detect the configuration

### Step 3: Configure Environment Variables

In Vercel project settings, add:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

Get your API key from: https://aistudio.google.com/app/apikey

### Step 4: Deploy Settings

Vercel will automatically:
- Build the React frontend from `/frontend`
- Deploy the FastAPI backend from `/fastapi-app`
- Route `/api/*` to the backend
- Serve the frontend for all other routes

### Step 5: Deploy!

Click "Deploy" and wait ~2 minutes.

Your app will be live at: `https://ecolens-agent.vercel.app`

---

## Alternative: Separate Deployments

### Frontend (Vercel/Netlify)

```bash
cd frontend
npm install
npm run build
```

Deploy the `dist/` folder.

Set environment variable:
```
VITE_API_URL=https://your-backend-url.com
```

### Backend (Railway/Render/Fly.io)

```bash
cd fastapi-app
pip install -r requirements.txt
```

Set environment variable:
```
GOOGLE_API_KEY=your_api_key
```

Run command:
```
uvicorn app:app --host 0.0.0.0 --port $PORT
```

---

## Local Development

### Terminal 1 - Backend
```bash
cd fastapi-app
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

### Terminal 2 - Frontend
```bash
cd frontend
npm install
npm run dev
```

Visit: http://localhost:3000

---

## Environment Variables

### Required
- `GOOGLE_API_KEY` - Your Google Gemini API key

### Optional
- `PORT` - Server port (default: 8000)

---

## Troubleshooting

### "Model currently experiencing high demand" (503 Error)
This is a temporary issue with Google's Gemini API. The app now shows a user-friendly error message. Simply wait a few moments and try again. If it persists:
- Wait 30-60 seconds between attempts
- Try refreshing the page
- Check [Google AI Status](https://status.cloud.google.com/) for outages

### CORS Errors
Update `fastapi-app/app.py` CORS origins to include your frontend domain.

### API Key Not Working
1. Check the key is valid at https://aistudio.google.com
2. Ensure it's set in Vercel environment variables
3. Redeploy after adding the variable

### Build Failures
- Frontend: Check Node.js version (18+)
- Backend: Check Python version (3.10+)

---

## Rate Limits

- `/api/analyze`: 5 requests/minute, 20/hour per IP
- `/health`: 60 requests/minute
- Other endpoints: 30 requests/minute

For production, consider:
- Redis-backed rate limiting
- User authentication
- Database for persistent storage

---

## Next Steps

1. ✅ Deploy to Vercel
2. Test the live app
3. Share the URL!
4. Monitor usage in Vercel dashboard
