#!/usr/bin/env python3
"""
Generate cute kawaii calendar illustrations for every day of 2026
"""

import os
import time
import subprocess
from datetime import datetime, timedelta

# Month configurations
MONTHS = [
    ("jan", "JAN", 31),
    ("feb", "FEB", 28),  # 2026 is not a leap year
    ("mar", "MAR", 31),
    ("apr", "APR", 30),
    ("may", "MAY", 31),
    ("jun", "JUN", 30),
    ("jul", "JUL", 31),
    ("aug", "AUG", 31),
    ("sep", "SEP", 30),
    ("oct", "OCT", 31),
    ("nov", "NOV", 30),
    ("dec", "DEC", 31),
]

# Cute subjects for variety (cycle through these)
SUBJECTS = [
    "tiny pastel blue cloud with sweet smile and rosy cheeks",
    "adorable smiling sun with soft yellow glow and pink cheeks",
    "cute sleepy moon with closed eyes and gentle smile",
    "tiny happy star with sparkles and rosy cheeks",
    "sweet smiling raindrop with soft blue color",
    "cozy warm cup of tea with steam hearts",
    "adorable sleeping cat curled up peacefully",
    "tiny floating balloon bouquet with happy face",
    "cute smiling flower with soft petals",
    "sweet little bird with fluffy feathers",
    "tiny happy mushroom with spots",
    "adorable smiling heart with soft glow",
    "cute floating feather with gentle swirl",
    "tiny happy acorn with little cap",
    "sweet smiling leaf with soft colors",
    "adorable tiny planet with rings and smile",
    "cute smiling rainbow with soft arcs",
    "tiny happy snowflake with delicate pattern",
    "sweet smiling butterfly with pastel wings",
    "adorable tiny book with bookmark smile",
    "cute smiling ice cream cone with sprinkles",
    "tiny happy cactus in a pot",
    "sweet smiling cupcake with frosting",
    "adorable tiny ghost with friendly smile",
    "cute smiling apple with leaf",
    "tiny happy pumpkin with gentle glow",
    "sweet smiling strawberry with seeds",
    "adorable tiny umbrella with raindrops",
    "cute smiling watermelon slice",
    "tiny happy cherry pair with stems",
    "sweet smiling donut with sprinkles",
]


def get_digit_balloons(day):
    """Generate balloon number description for a given day"""
    day_str = f"{day:02d}"
    digit1, digit2 = day_str[0], day_str[1]
    
    colors = ["soft peach", "soft pink", "soft lavender", "soft mint", "soft coral"]
    color1 = colors[int(digit1) % len(colors)]
    color2 = colors[int(digit2) % len(colors)]
    
    return f'balloon numbers "{digit1}" ({color1}) and "{digit2}" ({color2})'


def generate_prompt(month_abbr, day, subject):
    """Generate the image prompt for a specific date"""
    balloons = get_digit_balloons(day)
    
    prompt = f"""Cute minimal kawaii illustration: {subject}, holding {balloons}. 
Text "{month_abbr}" at bottom in rounded bubbly letters with soft outline. 
Light cream/beige background, flat illustration style, soft shading, kawaii-inspired, 
peaceful comforting mood, centered composition, icon-like, pastel color palette, 
simple shapes, not detailed, wholesome aesthetic."""
    
    return " ".join(prompt.split())  # Clean up whitespace


def main():
    base_dir = "/Users/azmatsiddique/Desktop/thelife/calendar_2026"
    
    print("🎨 Starting calendar illustration generation for 2026...")
    print(f"📁 Output directory: {base_dir}\n")
    
    total_images = 0
    subject_index = 0
    
    for month_folder, month_abbr, days in MONTHS:
        month_dir = os.path.join(base_dir, month_folder)
        os.makedirs(month_dir, exist_ok=True)
        
        print(f"\n{'='*60}")
        print(f"📅 Generating {month_abbr} ({days} days)")
        print(f"{'='*60}")
        
        for day in range(1, days + 1):
            # Cycle through subjects for variety
            subject = SUBJECTS[subject_index % len(SUBJECTS)]
            subject_index += 1
            
            filename = f"{month_folder}_{day:02d}.png"
            filepath = os.path.join(month_dir, filename)
            
            # Skip if already exists
            if os.path.exists(filepath):
                print(f"  ✓ {month_abbr} {day:02d} - Already exists, skipping")
                total_images += 1
                continue
            
            prompt = generate_prompt(month_abbr, day, subject)
            
            print(f"  🎨 Generating {month_abbr} {day:02d}...", end=" ", flush=True)
            
            # Here you would call your image generation API
            # For now, this is a placeholder that shows the structure
            print(f"[Subject: {subject[:30]}...]")
            
            # Simulate API call with rate limiting
            time.sleep(0.5)  # Adjust based on your API rate limits
            
            total_images += 1
            
            # Progress update every 10 images
            if total_images % 10 == 0:
                print(f"\n  📊 Progress: {total_images}/365 images generated ({total_images/365*100:.1f}%)\n")
    
    print(f"\n{'='*60}")
    print(f"✨ Complete! Generated {total_images} calendar illustrations")
    print(f"📁 Saved to: {base_dir}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
