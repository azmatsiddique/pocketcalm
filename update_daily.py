import os
import shutil
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
calendar_dir = os.path.join(base_dir, "calendar_2026")
public_dir = os.path.join(base_dir, "website", "public")
daily_path = os.path.join(public_dir, "daily.png")

def update_daily_wallpaper():
    now = datetime.now()
    month_slug = now.strftime("%b").lower() # e.g. "mar"
    day_slug = now.strftime("%d") # e.g. "07"
    
    # Target file pattern: calendar_2026/mar/mar_07.png
    source_filename = f"{month_slug}_{day_slug}.png"
    source_path = os.path.join(calendar_dir, month_slug, source_filename)
    
    if os.path.exists(source_path):
        # Copy to public/daily.png
        shutil.copy2(source_path, daily_path)
        print(f"✅ Successfully updated daily wallpaper to {source_filename}")
    else:
        print(f"⚠️ Could not find wallpaper for today: {source_path}")

if __name__ == "__main__":
    if not os.path.exists(public_dir):
        os.makedirs(public_dir)
    update_daily_wallpaper()
