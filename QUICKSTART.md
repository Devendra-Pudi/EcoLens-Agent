# ⚡ Quick Start Guide

## 🎯 Get Running in 5 Minutes

### 1. Clone the Repository
```bash
git clone https://github.com/Devendra-Pudi/EcoLens-Agent.git
cd EcoLens-Agent
```

### 2. Get Your API Key
Visit https://aistudio.google.com/app/apikey and create a free API key.

### 3. Configure Environment
Create `.env` file in the root directory:
```bash
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

### 4. Start Backend
```bash
cd fastapi-app
pip install -r requirements.txt
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

### 5. Start Frontend (New Terminal)
```bash
cd frontend
npm install
npm run dev
```

### 6. Open Your Browser
Visit: http://localhost:3000

### 7. Test It!
1. Upload a photo of any waste item
2. Click "Analyze with EcoLens"
3. Get instant AI-powered analysis!

---

## 🌐 Deploy to Vercel (2 Minutes)

1. Fork this repo on GitHub
2. Go to [vercel.com](https://vercel.com) and import your fork
3. Add environment variable: `GOOGLE_API_KEY`
4. Click Deploy!

Done! Your app is live at `https://your-project.vercel.app`

---

## 📱 Usage

### Upload Methods
- Click the upload area
- Drag and drop an image
- Supported: JPEG, PNG, GIF (max 20MB)

### What You Get
- 🔬 Material identification
- 👮 Disposal instructions
- 🎨 Creative upcycling ideas
- 📄 Downloadable report

---

## 🆘 Need Help?

- Check [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment guide
- Check [README.md](./README.md) for full documentation
- Open an issue on GitHub

---

## 🎉 That's It!

You now have a fully functional AI-powered waste analyst running locally or in the cloud!
