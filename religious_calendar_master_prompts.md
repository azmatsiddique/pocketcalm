# PocketCalm Global - Religious Master Prompts

This document contains the master templates for religious-themed calendar illustrations (Hindu, Muslim, and Christian).

---

## 1. Hindu-Inspired Calendar Illustration Prompt
**Style Match**: image_6.png
**Usage**: Populate the `[Insert Devanagari Shloka]`, `[Insert English Translation]`, `[Insert MONTH]`, and `[Insert Deity]` placeholders.

**Prompt**:
A symmetrical, ornamental vector illustration in a traditional Hindu style, divided into two panels on a cream-colored background.

**Left Panel**: Features a detailed, ornate traditional Hindu archway with pillars. The arch is decorated with intricate blue, gold, and red paisley patterns, small hanging lamps (diyas), and stylized floral garlands. Large red and pink lotus flowers are at the base, flanked by two stylized, fan-tailed peacocks standing on a traditional rug. Devanagari text is in the center-top of the arch, with the English translation directly below it: "[Insert Devanagari Shloka]\n[Insert English Translation]". At the very bottom, centered, is the word "[Insert MONTH]" in large, bubble-gum pink letters with a dark outline.

**Right Panel**: Features a symmetrical, circular floral and icon wreath design. The wreath is composed of pink lotus flowers, white jasmine flowers, and green leaves. At the very top center is a detailed Kalash (water pot with a coconut). To the top-left and top-right are small, circular icons of [Insert Deity 1, e.g., Hanuman] and [Insert Deity 2, e.g., Shiva], each within a decorated medallion. Two tridents (trishuls) with diyas stand vertically outside the circle. At the center is a large, central Om symbol. The area inside the circle is an open temple courtyard. Centered Devanagari text is below the Om symbol, with the English translation directly below it: "[Insert Devanagari Shloka]\n[Insert English Translation]". At the very bottom, centered, is the word "[Insert MONTH]" in large, dark blue letters with a blue outline.

**Aesthetic**: The entire illustration has soft, clean vector lines, a warm color palette (pink, orange, teal, gold, cream), and a respectful, devotional feel.

---

## 2. Muslim-Inspired Calendar Illustration Prompt
**Style Match**: Matches structure of the previous design with Muslim iconography.
**Usage**: Populate the `[Insert Arabic Dua]`, `[Insert English Translation]`, and `[Insert MONTH]` placeholders.

**Prompt**:
A symmetrical, ornamental vector illustration in a traditional Islamic and Mughal style, divided into two panels on a cream-colored background.

**Left Panel**: Features a detailed, ornate traditional Islamic archway (Iwan-style) with patterned blue and gold tilework and intricate arabesque designs. A large calligraphic Thuluth-style script in Arabic reads "[Insert Arabic Dua, e.g., الله أكبر]" at the center-top of the arch, with the English translation directly below it: "[Insert English Translation]". A traditional patterned prayer rug is at the base, flanked by two stylized, golden palm trees and crescent moon motifs. At the very bottom, centered, is the word "[Insert MONTH]" in large, bubble-gum pink letters with a dark outline.

**Right Panel**: Features a symmetrical, circular geometric arabesque and calligraphic wreath design. The wreath is composed of gold geometric patterns (Star of David and other polygons), small, smiling crescent moon and star icons, and delicate gold floral elements. At the top center, within the wreath, is a detailed medallion containing stylized Arabic calligraphy. Below it is the main text area. A beautiful Arabic text in Naskh-style script reads: "[Insert Arabic Dua]\n[Insert Arabic Dua]". The English translation is centered directly below the Arabic script: "[Insert English Translation]\n[Insert English Translation]". At the very bottom, centered, is the word "[Insert MONTH]" in large, dark blue letters with a blue outline.

**Aesthetic**: The entire illustration has clean vector lines, a cool and warm color palette (deep blue, turquoise, emerald green, gold, cream), and a respectful, spiritual feel, complementing the previous design.

---

## 3. Christian-Inspired Calendar Illustration Prompt
**Style Match**: Next design in the series.
**Usage**: Populate the `[Insert Verse/Text]` and `[Insert MONTH]` placeholders.

**Prompt**:
A symmetrical, ornamental vector illustration in a traditional Christian and ecclesiastical art style, divided into two distinct panels on a uniform cream-colored background. The entire composition has soft, clean vector lines and a warm, spiritual aesthetic.

**Left Panel**: Features a detailed, ornate traditional Christian church facade with stone pillars and a central pointed arch. The arch itself is framed by complex floral and ivy carvings, stylized grapes, and subtle scrollwork in blues, golds, and teals. Flanking the central arch are two vertical stained-glass window panels depicting abstract floral patterns and stylized crosses. A central ornate brass or copper incense burner hangs inside the arch. At the base, flanking the arch, are two stylized peacocks, but with a different posture than the reference, looking up toward the arch on a patterned chancel floor. Inside the central arch, the central text is a Bible verse or prayer (e.g., "Faith, Hope, and Love"), with the English translation directly below it: "[Insert Verse/Text]". At the very bottom, centered, is the word "[Insert MONTH]" in large, bubble-gum pink letters with a dark outline (matching the style and placement in image_6.png).

**Right Panel**: Features a complex, symmetrical circular stained-glass window design. The frame of the circle is composed of interwoven green and teal grapevines, white lily flowers, and small gold cross motifs. At the very top center of the circle, where the Kalash was, is a stylized Holy Spirit dove, descending with a nimbus of light. Inside the circle, forming a canopy, is a detailed stained-glass depiction of a stylized, peaceful, sunlit interior of a cathedral with a vaulted ceiling. At the top of this inner area is a large, central Cross symbol. Below the Cross, replacing the shloka text, is the central text for a common Christian prayer or verse (e.g., "The Lord is my Shepherd, I shall not want."), with the English translation directly below it: "[Insert Verse/Text]". Flanking the central design are two decorative candlesticks. At the very bottom, centered, is the word "[Insert MONTH]" in large, dark blue letters with a blue outline (matching the style and placement in image_6.png).

---

## 4. Website Creation Prompt (Technical Requirement)
**Baseline**: Reference the architecture in the existing `/website` folder (Vite + React 19).
**Goal**: Expand the current single-view calendar into a global multi-faith platform.

**Prompt**:
"Build a multi-faith wallpaper application based on the Vite + React architecture found in the `/website` directory.

**Key Features**:
1.  **Multi-Faith Engine**: Implement a global state or context to switch between Hindu, Muslim, and Christian themes. The UI should dynamically update its primary color tokens and asset paths based on this selection.
2.  **Gender Variation**: Add a 'Character Type' toggle (Male/Female) that swaps the central character in the wallpaper preview and download link.
3.  **Modern UI Layout**:
    - **Header**: Navigation for Religion and Gender selection with smooth micro-animations.
    - **Hero Section**: Large 'Today’s Wallpaper' display card with a glassmorphism effect.
    - **Calendar Grid**: A monthly grid view that tracks the full 365 days of 2026.
4.  **Aesthetic Continuity**: Retain the 'kawaii minimal' design system (rounded corners, pastel backgrounds, bubbly typography) but customize the accents for each religion:
    - **Hindu**: Saffron and lotus pink highlights.
    - **Muslim**: Emerald green and gold accents.
    - **Christian**: Sky blue and pure white accents.
5.  **Performance & Deployment**: Utilize the existing `vercel.json` and Vite build configuration for serverless deployment on Vercel, ensuring fast image loading via public asset optimization."
