#!/usr/bin/env python3
"""
Generate all 365 calendar illustration prompts for 2026
Output: JSON file with all prompts ready for batch processing
"""

import json
from datetime import datetime, timedelta

# Month configurations
MONTHS = [
    ("jan", "JAN", 31), ("feb", "FEB", 28), ("mar", "MAR", 31),
    ("apr", "APR", 30), ("may", "MAY", 31), ("jun", "JUN", 30),
    ("jul", "JUL", 31), ("aug", "AUG", 31), ("sep", "SEP", 30),
    ("oct", "OCT", 31), ("nov", "NOV", 30), ("dec", "DEC", 31),
]

# Cute subjects for variety (31 subjects, cycling through the year)
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
    
    prompt = f"""Cute minimal kawaii illustration: {subject}, holding {balloons}. Text "{month_abbr}" at bottom in rounded bubbly letters with soft outline. Light cream/beige background, flat illustration style, soft shading, kawaii-inspired, peaceful comforting mood, centered composition, icon-like, pastel color palette, simple shapes, not detailed, wholesome aesthetic."""
    
    return " ".join(prompt.split())

def main():
    all_prompts = []
    subject_index = 0
    
    for month_folder, month_abbr, days in MONTHS:
        for day in range(1, days + 1):
            subject = SUBJECTS[subject_index % len(SUBJECTS)]
            subject_index += 1
            
            prompt_data = {
                "date": f"2026-{MONTHS.index((month_folder, month_abbr, days)) + 1:02d}-{day:02d}",
                "filename": f"{month_folder}_{day:02d}.png",
                "month": month_abbr,
                "day": day,
                "subject": subject,
                "prompt": generate_prompt(month_abbr, day, subject),
                "folder": month_folder
            }
            
            all_prompts.append(prompt_data)
    
    # Save to JSON
    output_file = "calendar_2026_prompts.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_prompts, f, indent=2, ensure_ascii=False)
    
    print(f"✨ Generated {len(all_prompts)} prompts")
    print(f"📁 Saved to: {output_file}")
    
    # Also create a markdown version for easy reading
    md_output = "# Calendar 2026 - All Prompts\n\n"
    md_output += f"Total: {len(all_prompts)} illustrations\n\n"
    
    current_month = None
    for p in all_prompts:
        if p['month'] != current_month:
            current_month = p['month']
            md_output += f"\n## {current_month}\n\n"
        
        md_output += f"### {p['filename']}\n"
        md_output += f"**Subject:** {p['subject']}\n\n"
        md_output += f"**Prompt:**\n```\n{p['prompt']}\n```\n\n"
    
    md_file = "calendar_2026_prompts.md"
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_output)
    
    print(f"📄 Also saved markdown version to: {md_file}")

if __name__ == "__main__":
    main()
