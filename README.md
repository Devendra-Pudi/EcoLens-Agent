<div align="center">

# 🌿 EcoLens Agent
### Intelligent Waste Analyst — Powered by Multi-Agent AI

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://ecolens-agent.vercel.app)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

> *Upload an image. Identify waste. Get actionable eco-friendly recommendations — instantly.*

</div>

---

## 📖 Overview

**EcoLens Agent** is an AI-powered web application that analyzes waste from uploaded images and returns intelligent, eco-friendly disposal and recycling recommendations. It leverages a **multi-agent AI architecture** inspired by the characters from WALL-E, with each agent handling a distinct phase of the analysis pipeline.

---

## 🤖 Agent Architecture

| Agent | Role |
|-------|------|
| 🤖 **Wall-E** | Vision agent — identifies and classifies waste items from the image |
| 🌿 **Eve** | Sustainability agent — generates eco-friendly recommendations |
| 🔧 **MacGyver** | Creativity agent — suggests DIY upcycling and repurposing ideas |

---

## ✨ Features

- 📸 **Image-based waste detection** — upload any photo for instant analysis
- 🤖 **Multi-agent pipeline** — specialized agents collaborate for richer output
- ♻️ **Eco-friendly recommendations** — recycling, composting, upcycling suggestions
- ⚡ **Fast API backend** — rate-limited FastAPI server with CORS support
- 🌐 **Responsive React frontend** — built with Vite + Tailwind CSS
- 🚀 **Deployed on Vercel** — live and accessible anywhere

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React, Vite, Tailwind CSS |
| Backend | Python, FastAPI |
| AI Model | Google Gemini (Vision + Text) |
| Deployment | Vercel (Frontend), Vercel Functions (Backend) |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- Google Gemini API Key

### Installation

```bash
# Clone the repository
git clone https://github.com/Devendra-Pudi/EcoLens-Agent.git
cd EcoLens-Agent

# Backend setup
cd fastapi-app
pip install -r requirements.txt
echo "GEMINI_API_KEY=your_key_here" > .env
uvicorn main:app --reload

# Frontend setup (new terminal)
cd ../frontend
npm install
npm run dev
```

Open `http://localhost:5173` in your browser.

---

## 📁 Project Structure

```
EcoLens-Agent/
├── core/               # Shared agent logic & utilities
├── fastapi-app/        # FastAPI backend (API routes, agents)
├── frontend/           # React + Vite + Tailwind frontend
├── deployment/         # Vercel deployment config
├── tests/              # Unit tests
├── docs/               # Documentation
└── QUICKSTART.md       # Quick setup guide
```

---

## 🌍 Live Demo

**→ [ecolens-agent.vercel.app](https://ecolens-agent.vercel.app)**

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with 💚 for a greener planet by [Devendra Prasad Pudi](https://github.com/Devendra-Pudi)

⭐ Star this repo if you found it useful!

</div>
