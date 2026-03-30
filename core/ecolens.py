"""
EcoLens - The Intelligent Waste Analyst
A Multimodal Multi-Agent System for Smart Waste Management
"""

import os
from pathlib import Path
from google import genai
from google.genai import types

# ---------------------------------------------------------
# 🔑 API CONFIGURATION
# ---------------------------------------------------------
_client = None

def configure_api(api_key=None):
    """Configure the Gemini API"""
    global _client
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
    elif "GOOGLE_API_KEY" not in os.environ:
        raise ValueError("Please set GOOGLE_API_KEY environment variable or pass api_key parameter")

    _client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
    print("✅ API Configured")
    return _client

def get_client():
    global _client
    if _client is None:
        configure_api()
    return _client

# We use 2.5 Flash because it is highly optimized for Image Analysis + Low Latency
MODEL_NAME = "gemini-2.5-flash"

# ---------------------------------------------------------
# 📸 IMAGE HANDLING
# ---------------------------------------------------------
def load_image_from_path(path_to_image):
    """Load an image file and prepare it for Gemini"""
    path = Path(path_to_image)
    if not path.exists():
        raise FileNotFoundError(f"Could not find image: {path_to_image}")

    # Detect mime type from extension
    ext = path.suffix.lower()
    mime_map = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".gif": "image/gif"}
    mime_type = mime_map.get(ext, "image/jpeg")

    img_data = path.read_bytes()
    return types.Part.from_bytes(data=img_data, mime_type=mime_type)

print("✅ Image Loader Ready")

# ---------------------------------------------------------
# 🤖 MULTIMODAL AGENT CLASS
# ---------------------------------------------------------
class MultimodalAgent:
    """An agent that can process both text and image inputs"""

    def __init__(self, name, role, system_instruction):
        self.name = name
        self.role = role
        self.system_instruction = system_instruction

    def analyze(self, inputs):
        """
        inputs: a string, a Part, or a list containing both.
        """
        print(f"👁️ {self.name} ({self.role}) is analyzing...")
        client = get_client()

        # Normalize inputs to a list
        if not isinstance(inputs, list):
            inputs = [inputs]

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=inputs,
            config=types.GenerateContentConfig(
                system_instruction=self.system_instruction
            )
        )
        return response.text

# ---------------------------------------------------------
# 🌍 THE ECO-TEAM: THREE SPECIALIZED AGENTS
# ---------------------------------------------------------

scientist_agent = MultimodalAgent(
    "Wall-E", "Material Scientist",
    """You are a Material Scientist expert in waste management.
Your input will be an IMAGE of a piece of trash/object.
Your job is to output a technical description:

1. Identify the primary material (e.g., Polypropylene plastic, Corrugated Cardboard, Aluminum).
2. Identify the condition (Clean, Greasy, Food-soiled, Broken).
3. Identify if it is a composite item (e.g., a coffee cup with a plastic lid).

Be precise and factual."""
)

officer_agent = MultimodalAgent(
    "Eve", "Compliance Officer",
    """You are the Waste Compliance Officer.
You receive a technical description of an item.
Determine the disposal method based on standard strict recycling rules:

- Food-soiled cardboard -> Compost (NOT Recycling).
- Clean cardboard -> Recycling.
- Plastic bags -> Store Drop-off (NOT Curbside).
- Electronics -> E-Waste Facility.

Output:
**VERDICT:** [RECYCLE / COMPOST / LANDFILL / SPECIAL FACILITY]
**REASONING:** Brief explanation why."""
)

upcycler_agent = MultimodalAgent(
    "MacGyver", "Upcycling Expert",
    """You are a DIY Creativity Expert.
You receive a description of a 'trash' item.
Suggest 2 creative, fun, and practical ways to UPCYCLE (reuse) this item at home
instead of throwing it away.

Make the ideas sound fun and easy to do."""
)

# ---------------------------------------------------------
# 🔄 ORCHESTRATION PIPELINE
# ---------------------------------------------------------
def run_ecolens_pipeline(image_path):
    """
    Main pipeline that orchestrates all three agents:
    1. Vision analysis (Wall-E)
    2. Compliance check (Eve)
    3. Upcycling ideas (MacGyver)
    """
    print(f"\n♻️ Starting EcoLens Analysis on: {image_path}")
    print("=" * 60)

    # 0. Load Image
    image_part = load_image_from_path(image_path)
    print("✅ Image loaded successfully\n")

    # 1. VISION ANALYSIS
    material_analysis = scientist_agent.analyze([
        "Describe this object for recycling purposes:",
        image_part
    ])
    print(f"\n🔬 Wall-E Analysis:\n{'-'*60}\n{material_analysis}\n{'-'*60}")

    # 2. COMPLIANCE CHECK
    verdict = officer_agent.analyze(
        f"Based on this description, how do I dispose of it?\n\n{material_analysis}"
    )
    print(f"\n👮 Eve Verdict:\n{'-'*60}\n{verdict}\n{'-'*60}")

    # 3. UPCYCLING IDEAS
    ideas = upcycler_agent.analyze(
        f"Give me ideas to reuse this:\n\n{material_analysis}"
    )
    print(f"\n🎨 MacGyver Ideas:\n{'-'*60}\n{ideas}\n{'-'*60}")

    print("\n✅ EcoLens Analysis Complete!")

    return {
        "material_analysis": material_analysis,
        "verdict": verdict,
        "upcycling_ideas": ideas
    }

# ---------------------------------------------------------
# 🚀 MAIN EXECUTION
# ---------------------------------------------------------
if __name__ == "__main__":
    print("♻️ EcoLens - The Intelligent Waste Analyst")
    print("=" * 60)
    configure_api()
    print("\n📝 To use EcoLens, call: run_ecolens_pipeline('path/to/image.jpg')")
