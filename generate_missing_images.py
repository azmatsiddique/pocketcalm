#!/usr/bin/env python3
"""
Helper script to identify missing calendar images.
Reads calendar_2026_prompts.json and checks if the corresponding file exists.
Prints the prompt and details for missing files.
"""

import json
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Find missing calendar images")
    parser.add_argument("--month", help="Filter by month abbreviation (e.g., JAN, FEB)", default=None)
    args = parser.parse_args()

    base_dir = "/Users/azmatsiddique/Desktop/data/thelife/calendar_2026"
    prompts_file = "/Users/azmatsiddique/Desktop/data/thelife/calendar_2026_prompts.json"

    with open(prompts_file, 'r', encoding='utf-8') as f:
        prompts = json.load(f)

    missing_count = 0
    total_count = 0

    print(f"Checking for missing images in {base_dir}...")
    
    for item in prompts:
        if args.month and item['month'] != args.month.upper():
            continue
            
        total_count += 1
        month_dir = item['folder']
        filename = item['filename']
        filepath = os.path.join(base_dir, month_dir, filename)

        if not os.path.exists(filepath):
            missing_count += 1
            print(f"\n[MISSING] {item['date']} - {filename}")
            print(f"Subject: {item['subject']}")
            print(f"Prompt: {item['prompt']}")

    print(f"\n{'-'*40}")
    print(f"Found {missing_count} missing images out of {total_count} checked.")

if __name__ == "__main__":
    main()
