# ♻️ EcoLens - The Intelligent Waste Analyst

**A Multimodal Multi-Agent System for Smart Waste Management**

## 🎯 The Problem

"Wishcycling"—tossing items in the recycling bin hoping they are recyclable when they aren't (like greasy pizza boxes or broken glass)—actually contaminates entire batches of recycling, sending tons of usable material to landfills. People want to be sustainable, but material science is complex and local rules are confusing.

## 💡 The Solution

EcoLens is a Multimodal Multi-Agent System. Instead of asking users to describe their trash, they simply snap a photo.

### The Three-Agent Team:

1. **Wall-E (Material Scientist)**: Uses Gemini 1.5's vision capabilities to analyze the object's material, cleanliness (e.g., food residue), and composition.

2. **Eve (Compliance Officer)**: Determines the correct disposal method (Compost, Recycle, Landfill, E-Waste) based on strict rules.

3. **MacGyver (Upcycler)**: Suggests DIY projects to reuse the item, extending its lifecycle before disposal.

## 🏗️ Architecture

```
[User Photo] 
    ↓
[Gemini Vision Agent - Wall-E] → Material Analysis (Text)
    ↓
    ├─→ [Policy Agent - Eve] → Disposal Verdict
    └─→ [Creative Agent - MacGyver] → Upcycling Ideas
```

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Set up your API key

```bash
# Option 1: Environment variable
export GOOGLE_API_KEY="your_api_key_here"

# Option 2: Windows
set GOOGLE_API_KEY=your_api_key_here
```

### Run the Demo

```bash
python demo.py
```

This will:
- Download sample images (plastic bottle, pizza box)
- Run the full EcoLens pipeline on each image
- Show material analysis, disposal verdict, and upcycling ideas

### Use in Your Code

```python
from ecolens import configure_api, run_ecolens_pipeline

# Configure API
configure_api("your_api_key_here")

# Analyze any image
results = run_ecolens_pipeline("path/to/your/image.jpg")
```

## 🎨 Features

- **Multimodal Intelligence**: Uses computer vision to assess objects directly, reducing user friction
- **Agent Specialization**: Each agent has a distinct role and expertise
- **Chain of Thought**: Visual analysis flows into policy engine, then into creative engine
- **Real-World Impact**: Solves recycling contamination with technology that feels "magic"

## 🔮 Future Improvements

- **GPS Integration**: Automatically load specific recycling rules for user's city/municipality
- **Gamification**: Award points for every item correctly scanned and upcycled
- **Mobile App**: Native iOS/Android app with camera integration
- **Community Database**: Crowdsourced local recycling rules and upcycling ideas

## 📊 Why EcoLens Stands Out

1. **Multimodal**: While other projects rely on text input, EcoLens uses Computer Vision
2. **Specialized Agents**: Three distinct agents with clear responsibilities
3. **Practical Impact**: Addresses a measurable problem (recycling contamination)
4. **User-Friendly**: Just snap a photo—no complex descriptions needed

## 🛠️ Tech Stack

- **Gemini 1.5 Flash**: Optimized for image analysis + low latency
- **Python**: Core implementation language
- **Multi-Agent Architecture**: Specialized agents working in sequence

## 📝 License

MIT License - Feel free to use this for good!

## 👤 Author

[Your Name]

---

**Track**: Agents for Good  
**Theme**: Sustainability & Computer Vision
