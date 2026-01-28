# Project: Coal Quality Characterization & Industrial Suitability Tool
# Author: [Mohsin Mustafa]
# Logic: Based on ASTM D388 Standards & Peshawar University Research Data

def get_coal_rank(calorific_value_kcal):
    """
    Converts kcal/kg to MJ/kg and determines the coal rank 
    based on the classification table in Source [4].
    """
    # Standard conversion factor: 1 kcal/kg = 0.004184 MJ/kg [5]
    mj_kg = calorific_value_kcal * 0.004184
    
    if mj_kg < 15:
        return "Peat", mj_kg
    elif 15 <= mj_kg < 19:
        return "Lignite", mj_kg
    elif 19 <= mj_kg < 26:
        return "Sub-bituminous", mj_kg
    elif 26 <= mj_kg < 35:
        return "Bituminous", mj_kg
    else:
        return "Anthracite", mj_kg

def get_industrial_advice(rank, sulfur, ash):
    """
    Provides industrial recommendations based on comparative 
    analysis from Source [6] and [7].
    """
    advice = []
    
    # Check for energy generation suitability [6, 8]
    if rank in ["Sub-bituminous", "Bituminous"]:
        advice.append("Recommended for local power generation.")
    
    # Environmental check based on sulfur content (~1.2%) [7, 8]
    if sulfur <= 1.2:
        advice.append("Environmentally friendly due to low sulfur emissions.")
    else:
        advice.append("Higher sulfur detected; blending with high-grade coal required.")
        
    # Industrial suitability (Steel/Coke production) [6]
    if ash > 10:
        advice.append("Not suitable for Pak Steel Mills (Ash content too high for coke).")
    
    return " | ".join(advice)

# --- Main Data Processing (Laboratory Samples from Source [9]) ---

samples = [
    {"id": "Sample 1", "kcal": 6972.65, "sulfur": 1.1, "ash": 13.5},
    {"id": "Sample 2", "kcal": 5076.62, "sulfur": 1.3, "ash": 15.2},
    {"id": "Sample 3", "kcal": 5072.32, "sulfur": 1.0, "ash": 12.3},
    {"id": "Sample 4", "kcal": 4020.89, "sulfur": 1.9, "ash": 11.9},
]

print("=== DARA ADAM KHEL COAL CHARACTERIZATION REPORT ===\n")

for s in samples:
    rank, energy_mj = get_coal_rank(s["kcal"])
    industrial_note = get_industrial_advice(rank, s["sulfur"], s["ash"])
    
    print(f"ID: {s['id']}")
    print(f"Energy Potential: {energy_mj:.2f} MJ/kg")
    print(f"Classification: {rank}")
    print(f"Industrial Advice: {industrial_note}")
    print("-" * 50)
