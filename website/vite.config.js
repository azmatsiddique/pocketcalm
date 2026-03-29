import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Local dev plugin that mimics the Vercel /api/wallpaper function
const wallpaperApiPlugin = {
  name: 'wallpaper-api',
  configureServer(server) {
    server.middlewares.use('/api/wallpaper', (req, res) => {
      const now = new Date();
      const MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];
      const month = MONTHS[now.getMonth()];
      const day = String(now.getDate()).padStart(2, '0');
      const imagePath = `/calendar_2026/${month}/${month}_${day}.png`;
      res.writeHead(302, {
        'Location': imagePath,
        'Cache-Control': 'no-store',
      });
      res.end();
    });
  },
};

export default defineConfig({
  plugins: [react(), wallpaperApiPlugin],
  server: {
    host: true,
    port: 5173,
  }
})

