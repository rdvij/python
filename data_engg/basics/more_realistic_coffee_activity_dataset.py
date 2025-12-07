import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
NUM_FARMERS = 70
NUM_DAYS = 365
START_DATE = datetime(2024, 1, 1)

# Activities configuration
ACTIVITIES = [
    "watering", "fertilising", "harvesting", "pruning", "weeding", 
    "pest_control", "shade_management", "drying", "sorting", 
    "packaging", "transporting", "mulching", "grafting"
]

def get_season(date):
    """Determine season based on month (Northern Hemisphere tropical)"""
    month = date.month
    if month in [12, 1, 2]:
        return "dry_season"
    elif month in [3, 4, 5]:
        return "harvest_season"
    elif month in [6, 7, 8]:
        return "wet_season"
    else:  # 9, 10, 11
        return "post_harvest"

def get_temperature(season, base_temp=25):
    """Generate realistic temperature based on season"""
    season_variance = {
        "dry_season": (28, 35),
        "harvest_season": (24, 30),
        "wet_season": (20, 26),
        "post_harvest": (22, 28)
    }
    min_temp, max_temp = season_variance[season]
    return round(random.uniform(min_temp, max_temp), 1)

def should_perform_activity(activity, season, date, last_harvest_date):
    """Determine if an activity should be performed based on season and logic"""
    day_since_harvest = (date - last_harvest_date).days if last_harvest_date else 365
    
    # Activity probabilities by season
    probabilities = {
        "watering": {
            "dry_season": 0.8, "harvest_season": 0.4, 
            "wet_season": 0.1, "post_harvest": 0.5
        },
        "fertilising": {
            "dry_season": 0.15, "harvest_season": 0.05, 
            "wet_season": 0.25, "post_harvest": 0.2
        },
        "harvesting": {
            "dry_season": 0.0, "harvest_season": 0.6, 
            "wet_season": 0.0, "post_harvest": 0.0
        },
        "pruning": {
            "dry_season": 0.1, "harvest_season": 0.05, 
            "wet_season": 0.2, "post_harvest": 0.25
        },
        "weeding": {
            "dry_season": 0.2, "harvest_season": 0.15, 
            "wet_season": 0.35, "post_harvest": 0.25
        },
        "pest_control": {
            "dry_season": 0.12, "harvest_season": 0.1, 
            "wet_season": 0.2, "post_harvest": 0.15
        },
        "shade_management": {
            "dry_season": 0.08, "harvest_season": 0.05, 
            "wet_season": 0.12, "post_harvest": 0.1
        },
        "drying": {
            "dry_season": 0.0, "harvest_season": 0.0, 
            "wet_season": 0.0, "post_harvest": 0.0
        },
        "sorting": {
            "dry_season": 0.0, "harvest_season": 0.0, 
            "wet_season": 0.0, "post_harvest": 0.0
        },
        "packaging": {
            "dry_season": 0.0, "harvest_season": 0.0, 
            "wet_season": 0.0, "post_harvest": 0.0
        },
        "transporting": {
            "dry_season": 0.0, "harvest_season": 0.0, 
            "wet_season": 0.0, "post_harvest": 0.0
        },
        "mulching": {
            "dry_season": 0.15, "harvest_season": 0.1, 
            "wet_season": 0.08, "post_harvest": 0.12
        },
        "grafting": {
            "dry_season": 0.05, "harvest_season": 0.02, 
            "wet_season": 0.1, "post_harvest": 0.08
        }
    }
    
    # Post-harvest processing activities (occur within 7 days after harvest)
    if activity in ["drying", "sorting", "packaging", "transporting"]:
        if day_since_harvest <= 7:
            if activity == "drying":
                return random.random() < 0.7
            elif activity == "sorting" and day_since_harvest >= 2:
                return random.random() < 0.6
            elif activity == "packaging" and day_since_harvest >= 3:
                return random.random() < 0.5
            elif activity == "transporting" and day_since_harvest >= 4:
                return random.random() < 0.4
        return False
    
    # Regular activities
    return random.random() < probabilities[activity][season]

def get_activity_duration(activity):
    """Get realistic duration for each activity type"""
    durations = {
        "watering": (1, 3),
        "fertilising": (2, 4),
        "harvesting": (6, 10),
        "pruning": (3, 6),
        "weeding": (4, 7),
        "pest_control": (2, 4),
        "shade_management": (2, 5),
        "drying": (4, 8),
        "sorting": (5, 9),
        "packaging": (3, 6),
        "transporting": (2, 5),
        "mulching": (3, 6),
        "grafting": (2, 4)
    }
    min_dur, max_dur = durations[activity]
    return round(random.uniform(min_dur, max_dur), 1)

def get_yield(activity, season):
    """Generate yield only for harvesting activity"""
    if activity == "harvesting":
        # Harvest season yields are higher
        if season == "harvest_season":
            return round(random.uniform(150, 350), 1)
        else:
            return round(random.uniform(50, 150), 1)
    return 0

def get_npk_values(activity):
    """Generate NPK values for fertilising activity"""
    if activity == "fertilising":
        n = round(random.uniform(10, 30), 1)
        p = round(random.uniform(5, 20), 1)
        k = round(random.uniform(10, 25), 1)
        return f"{n}-{p}-{k}"
    return ""

# Generate data
data = []
farmer_harvest_dates = {f"F{i+1:03d}": None for i in range(NUM_FARMERS)}

for day_offset in range(NUM_DAYS):
    current_date = START_DATE + timedelta(days=day_offset)
    season = get_season(current_date)
    
    for farmer_num in range(NUM_FARMERS):
        farmer_id = f"F{farmer_num+1:03d}"
        
        # Each farmer performs 1-3 activities per day
        num_activities = random.choices([0, 1, 2, 3], weights=[0.3, 0.4, 0.2, 0.1])[0]
        
        # Shuffle activities to add randomness
        daily_activities = ACTIVITIES.copy()
        random.shuffle(daily_activities)
        
        activities_performed = 0
        for activity in daily_activities:
            if activities_performed >= num_activities:
                break
                
            if should_perform_activity(activity, season, current_date, 
                                     farmer_harvest_dates[farmer_id]):
                
                # Track harvest dates for post-harvest processing
                if activity == "harvesting":
                    farmer_harvest_dates[farmer_id] = current_date
                
                row = {
                    "farmer_id": farmer_id,
                    "activity_type": activity,
                    "activity_date": current_date.strftime("%Y-%m-%d"),
                    "season": season,
                    "temperature": get_temperature(season),
                    "duration_in_hours": get_activity_duration(activity),
                    "yield_kg": get_yield(activity, season),
                    "NPK": get_npk_values(activity)
                }
                data.append(row)
                activities_performed += 1

# Create DataFrame
df = pd.DataFrame(data)

# Sort by date and farmer_id
df = df.sort_values(["activity_date", "farmer_id"]).reset_index(drop=True)

# Save to CSV
output_file = "coffee_farm_activities.csv"
df.to_csv(output_file, index=False)

print(f"Generated {len(df)} activity records for {NUM_FARMERS} farmers over {NUM_DAYS} days")
print(f"\nData saved to: {output_file}")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head(10))
print(f"\nActivity distribution:")
print(df['activity_type'].value_counts())
print(f"\nSeason distribution:")
print(df['season'].value_counts())