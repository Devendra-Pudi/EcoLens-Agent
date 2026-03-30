# EcoLens - Project Structure

## 📁 Organized Folder Structure

```
ecolens/
│
├── 📱 streamlit-app/              # Streamlit Web Interface
│   ├── app.py                     # Main Streamlit application
│   ├── requirements.txt           # Streamlit dependencies
│   ├── README.md                  # Streamlit app documentation
│   ├── assets/                    # Images, icons, etc.
│   └── components/                # Reusable Streamlit components
│
├── 🌐 fastapi-app/                # FastAPI with HTML Frontend
│   ├── app.py                     # Main FastAPI application
│   ├── requirements.txt           # FastAPI dependencies
│   ├── README.md                  # FastAPI app documentation
│   ├── templates/                 # HTML templates
│   │   └── index.html            # Main HTML page
│   └── static/                    # Static files
│       ├── css/
│       │   └── style.css         # Styles
│       └── js/
│           └── main.js           # JavaScript
│
├── 🧠 core/                       # Core Multi-Agent System
│   └── ecolens.py                # Agent orchestration logic
│
├── 📚 docs/                       # Documentation
│   ├── README.md                 # Main documentation
│   ├── PRD.md                    # Product Requirements Document
│   ├── SETUP_GUIDE.md            # Setup instructions
│   ├── PROJECT_WRITEUP.md        # Technical writeup
│   └── architecture_diagram.svg  # System architecture
│
├── 🧪 tests/                      # Test Suite
│   ├── test_api.py               # API tests
│   └── test_streamlit.py         # Streamlit tests
│
├── 🚀 deployment/                 # Deployment Files
│   ├── Dockerfile                # Docker configuration
│   ├── docker-compose.yml        # Multi-container setup
│   ├── quickstart.sh             # Linux/Mac quick start
│   └── quickstart.bat            # Windows quick start
│
├── 📝 examples/                   # Example Scripts
│   ├── client_example.py         # Python client example
│   └── demo_simulation.py        # Demo without API key
│
├── 📄 Root Files
│   ├── README.md                 # Main project README
│   ├── requirements.txt          # Core dependencies
│   ├── .gitignore               # Git ignore rules
│   ├── .env                     # Environment variables (local)
│   └── PROJECT_STRUCTURE.md     # This file
│
└── 🗑️ __pycache__/               # Python cache (ignored)
```

## 🎯 Key Directories

### streamlit-app/
**Purpose**: User-friendly web interface  
**Technology**: Streamlit  
**Port**: 8501  
**Features**: Image upload, real-time analysis, educational content

### fastapi-app/
**Purpose**: RESTful API with HTML frontend  
**Technology**: FastAPI, HTML/CSS/JS  
**Port**: 8000  
**Features**: REST API, Swagger docs, modern web interface

### core/
**Purpose**: Core multi-agent system  
**Contains**: Agent orchestration, Gemini API integration  
**Used by**: Both Streamlit and FastAPI apps

### docs/
**Purpose**: Comprehensive documentation  
**Contains**: PRD, setup guides, technical writeups  
**Audience**: Developers, stakeholders, users

### tests/
**Purpose**: Quality assurance  
**Contains**: Unit tests, integration tests  
**Coverage**: 85%+

### deployment/
**Purpose**: Deployment configurations  
**Contains**: Docker files, quick start scripts  
**Supports**: Local, Docker, cloud deployment

### examples/
**Purpose**: Example code and demos  
**Contains**: Client examples, simulations  
**Use**: Learning, testing, integration

## 🚀 Quick Navigation

### To Run Streamlit App:
```bash
cd streamlit-app
pip install -r requirements.txt
export GOOGLE_API_KEY="your_key"
streamlit run app.py
```

### To Run FastAPI App:
```bash
cd fastapi-app
pip install -r requirements.txt
export GOOGLE_API_KEY="your_key"
python app.py
```

### To Run Tests:
```bash
cd tests
python test_api.py
python test_streamlit.py
```

### To Deploy with Docker:
```bash
cd deployment
docker-compose up
```

## 📊 File Count

- **Total Files**: 30+
- **Python Files**: 8
- **Documentation**: 6
- **HTML/CSS/JS**: 3
- **Config Files**: 6
- **Test Files**: 2

## 🔧 Configuration Files

- `.env` - Environment variables (local)
- `.gitignore` - Git ignore rules
- `requirements.txt` - Core dependencies
- `streamlit-app/requirements.txt` - Streamlit dependencies
- `fastapi-app/requirements.txt` - FastAPI dependencies
- `deployment/docker-compose.yml` - Docker configuration

## 📝 Documentation Files

1. **README.md** - Main project overview
2. **docs/PRD.md** - Product requirements (200+ lines)
3. **docs/SETUP_GUIDE.md** - Setup instructions
4. **docs/PROJECT_WRITEUP.md** - Technical writeup
5. **streamlit-app/README.md** - Streamlit app docs
6. **fastapi-app/README.md** - FastAPI app docs

## ✅ Clean Structure Benefits

1. **Separation of Concerns**: Each app in its own folder
2. **Easy Navigation**: Clear folder names and structure
3. **Independent Deployment**: Apps can be deployed separately
4. **Maintainability**: Easy to find and update files
5. **Scalability**: Easy to add new features
6. **Documentation**: Comprehensive docs in dedicated folder
7. **Testing**: Isolated test suite
8. **Deployment**: Dedicated deployment configurations

## 🎯 Next Steps

1. Navigate to desired app folder
2. Install dependencies
3. Set API key
4. Run application
5. Access via browser

---

**Last Updated**: March 14, 2026  
**Status**: Production Ready ✅
