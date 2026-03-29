/**
 * Vercel Serverless Function: /api/wallpaper
 * One permanent URL — redirects to today's illustration every day.
 */
export default function handler(req, res) {
    const now = new Date();
    const MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];
    const month = MONTHS[now.getMonth()];
    const day = String(now.getDate()).padStart(2, '0');

    const imagePath = `/calendar_2026/${month}/${month}_${day}.png`;

    res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate');
    res.redirect(302, imagePath);
}
