import { useState } from 'react';
import './index.css';

const today = new Date();
const timeStr = today.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: false });
const dateStr = today.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' });

// Compute today's image for the hero phone preview
const MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];
const month = MONTHS[today.getMonth()];
const day = String(today.getDate()).padStart(2, '0');
const DAILY_IMAGE = `/calendar_2026/${month}/${month}_${day}.png`;

// This URL never changes — Vercel API auto-picks today's image on the server
const SHORTCUT_URL = `${window.location.origin}/api/wallpaper`;

export default function App() {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(SHORTCUT_URL).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    });
  };

  return (
    <>
      <div className="bg-layer" />

      {/* NAV */}
      <nav className="nav">
        <div className="nav-logo">Pocket<span>Calm</span></div>
        <ul className="nav-links">
          <li><a href="#shortcuts">Shortcuts</a></li>
          <li><a href="#gallery">Gallery</a></li>
        </ul>
        <button className="btn btn-primary">Get Wallpaper</button>
      </nav>

      {/* HERO */}
      <section className="hero">
        <div>
          <div className="hero-eyebrow">
            <span className="dot" />
            2026 Daily Wallpapers
          </div>
          <h1 className="hero-title">
            Your Daily Dose<br />of <span className="gradient">Wholesome.</span>
          </h1>
          <p className="hero-sub">
            365 hand-curated kawaii illustrations — one new artwork automagically appears on your iPhone every single morning.
          </p>
          <div className="hero-ctas">
            <a href="#shortcuts" className="btn btn-primary">⚡ Setup Shortcut</a>
            <a href="#gallery" className="btn btn-ghost">View Gallery</a>
          </div>
        </div>

        <div className="hero-visual">
          <div className="glow-orb" />
          <div className="phone">
            <div className="phone-screen">
              <img src={DAILY_IMAGE} alt="Today's wallpaper" />
              <div className="phone-overlay" />
              <div className="phone-time">
                <div className="time">{timeStr}</div>
                <div className="date">{dateStr}</div>
              </div>
            </div>
          </div>
          <div className="pill-badge">
            <span className="icon">🖼️</span>
            <span>New art every day</span>
          </div>
        </div>
      </section>

      {/* SHORTCUTS SECTION */}
      <section id="shortcuts" className="shortcut-section">
        <div className="shortcut-grid">
          <div>
            <div className="section-label">iPhone Setup</div>
            <h2 className="section-title">Set it. Forget it.<br />Be wholesome.</h2>
            <p className="section-sub" style={{ marginBottom: '2rem' }}>
              Use the URL below inside any iOS Shortcuts automation to automatically change your wallpaper every day.
            </p>

            <div className="url-box">
              <div className="url-box-label">Permanent Shortcut URL — never changes ✓</div>
              <div className="url-row">
                <span className="url-text">{SHORTCUT_URL}</span>
                <button
                  className={`copy-btn ${copied ? 'copied' : ''}`}
                  onClick={handleCopy}
                >
                  {copied ? '✓ Copied!' : 'Copy'}
                </button>
              </div>
            </div>
          </div>

          <div className="steps">
            {[
              { num: '01', title: 'Open the Shortcuts App', desc: 'Tap Automation → New Automation → Time of Day (e.g. 6:00 AM).' },
              { num: '02', title: 'Get File from URL', desc: 'Add action "Get Contents of URL" and paste your copied link.' },
              { num: '03', title: 'Set Wallpaper', desc: 'Add "Set Wallpaper" action from the result. Toggle both Home & Lock screen.' },
              { num: '04', title: 'Wake up to Joy', desc: 'Every morning a fresh kawaii illustration greets you automatically.' },
            ].map(s => (
              <div key={s.num} className="step-card">
                <div className="step-num">{s.num}</div>
                <div>
                  <div className="step-title">{s.title}</div>
                  <div className="step-desc">{s.desc}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* GALLERY */}
      <section id="gallery" className="gallery-section">
        <div className="gallery-header">
          <div>
            <div className="section-label">Archives</div>
            <h2 className="section-title">365 Days of Joy</h2>
          </div>
          <p style={{ color: 'var(--muted)', fontSize: '0.9rem' }}>Scroll to explore →</p>
        </div>
        <div className="gallery-scroll">
          {[1, 2, 3, 4, 5, 6, 7].map(i => (
            <div key={i} className="gallery-card">
              <img
                src={`/calendar_2026/jan/jan_0${i}.png`}
                alt={`Day ${i}`}
              />
            </div>
          ))}
        </div>
      </section>

      <footer>
        © 2026 PocketCalm · Crafted with ☁️ &amp; kindness
      </footer>
    </>
  );
}
