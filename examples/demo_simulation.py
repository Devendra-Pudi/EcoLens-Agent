"""
EcoLens Demo Simulation
Shows how the multi-agent system works with simulated responses
"""

import time
import os

def print_header(text):
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)

def simulate_agent_thinking(agent_name, role):
    print(f"\n👁️ {agent_name} ({role}) is analyzing...")
    time.sleep(1)

def main():
    print_header("♻️ EcoLens - The Intelligent Waste Analyst")
    print("\nA Multimodal Multi-Agent System for Smart Waste Management")
    print("\n🎬 This is a SIMULATION showing how the agents work")
    print("   (To run with real AI, you need a Gemini API key)")
    
    # Test Case 1: Plastic Bottle
    print_header("TEST 1: Clean Plastic Bottle")
    
    print("\n📸 Input: Photo of a clean plastic water bottle")
    time.sleep(1)
    
    # Agent 1: Wall-E (Vision Analysis)
    simulate_agent_thinking("Wall-E", "Material Scientist")
    print("\n🔬 Wall-E Analysis:")
    print("-" * 60)
    print("""
Material Identification:
- Primary Material: PET (Polyethylene Terephthalate) plastic
- Resin Code: #1 (recyclable)
- Condition: Clean, no food residue
- Structure: Single-material bottle with removable cap
- Color: Clear/transparent
- Size: Standard 500ml water bottle
    """.strip())
    print("-" * 60)
    time.sleep(1)
    
    # Agent 2: Eve (Compliance Check)
    simulate_agent_thinking("Eve", "Compliance Officer")
    print("\n👮 Eve Verdict:")
    print("-" * 60)
    print("""
**VERDICT:** ♻️ RECYCLE (Curbside)

**REASONING:** 
Clean PET plastic (#1) is widely accepted in curbside recycling programs.
The bottle is free from contamination and is one of the most recyclable 
plastics. Remove the cap (also recyclable) and rinse before recycling.

**Instructions:**
1. Remove and recycle cap separately
2. Rinse bottle with water
3. Place in recycling bin
4. Do NOT crush (helps sorting machines)
    """.strip())
    print("-" * 60)
    time.sleep(1)
    
    # Agent 3: MacGyver (Upcycling Ideas)
    simulate_agent_thinking("MacGyver", "Upcycling Expert")
    print("\n🎨 MacGyver Ideas:")
    print("-" * 60)
    print("""
Before you recycle, consider these fun upcycling ideas:

💡 Idea 1: Mini Herb Garden
Cut the bottle in half. Use the bottom as a planter for herbs like basil 
or mint. Poke drainage holes in the bottom. Perfect for windowsill gardens!

💡 Idea 2: DIY Sprinkler
Poke small holes in the cap, fill with water, and squeeze to create a 
gentle sprinkler for delicate plants or a fun outdoor toy for kids.

🌱 Environmental Impact: Extending the bottle's life by just 1 month 
saves the energy equivalent of powering a LED bulb for 2 hours!
    """.strip())
    print("-" * 60)
    
    # Test Case 2: Pizza Box
    print_header("TEST 2: Greasy Pizza Box (Contamination Test)")
    
    print("\n📸 Input: Photo of a pizza box with grease stains")
    time.sleep(1)
    
    # Agent 1: Wall-E
    simulate_agent_thinking("Wall-E", "Material Scientist")
    print("\n🔬 Wall-E Analysis:")
    print("-" * 60)
    print("""
Material Identification:
- Primary Material: Corrugated cardboard
- Condition: CONTAMINATED - Heavy grease staining on bottom
- Composition: Mixed - Clean lid, soiled bottom
- Food Residue: Yes - cheese and oil stains visible
- Structure: Two-piece box (lid + bottom)
    """.strip())
    print("-" * 60)
    time.sleep(1)
    
    # Agent 2: Eve
    simulate_agent_thinking("Eve", "Compliance Officer")
    print("\n👮 Eve Verdict:")
    print("-" * 60)
    print("""
**VERDICT:** ⚠️ MIXED DISPOSAL

**REASONING:**
This is a classic "wishcycling" trap! Food-soiled cardboard CANNOT be 
recycled as the grease contaminates the recycling stream. However, the 
clean parts can be salvaged.

**Instructions:**
1. TEAR APART: Separate clean lid from greasy bottom
2. Clean lid → ♻️ RECYCLING BIN
3. Greasy bottom → 🗑️ COMPOST (if available) or LANDFILL
4. Remove any plastic windows or stickers first

⚠️ NEVER recycle greasy cardboard - it ruins entire batches!
    """.strip())
    print("-" * 60)
    time.sleep(1)
    
    # Agent 3: MacGyver
    simulate_agent_thinking("MacGyver", "Upcycling Expert")
    print("\n🎨 MacGyver Ideas:")
    print("-" * 60)
    print("""
Even contaminated cardboard has value:

💡 Idea 1: Compost Carbon Layer
Tear the greasy cardboard into strips and add to your compost bin. 
It's a "brown" carbon-rich material that balances "green" food scraps. 
The grease will break down naturally!

💡 Idea 2: Garden Weed Barrier
Use clean sections as biodegradable weed barriers in your garden. 
Place under mulch to suppress weeds. It will decompose over time, 
enriching the soil.

🌱 Fun Fact: Composting one pizza box saves 1.5 lbs of CO2 emissions 
compared to landfilling!
    """.strip())
    print("-" * 60)
    
    # Summary
    print_header("✅ Demo Complete!")
    print("""
🎯 Key Takeaways:

1. MULTIMODAL INPUT: Just snap a photo - no need to describe materials
2. AGENT SPECIALIZATION: Each agent has expertise
   - Wall-E: Visual analysis & material science
   - Eve: Recycling rules & compliance
   - MacGyver: Creative reuse ideas
3. REAL IMPACT: Reduces contamination & extends product lifecycles
4. CHAIN OF THOUGHT: Vision → Policy → Creativity

🚀 To run with REAL AI:
   1. Get a free Gemini API key: https://aistudio.google.com/apikey
   2. Set it: set GOOGLE_API_KEY=your_key_here
   3. Run: python demo.py

📚 Architecture: See architecture_diagram.svg for visual flow
    """.strip())
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
