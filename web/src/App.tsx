import { useRef, useState } from 'react';
import Hero from './Hero';
import Dashboard from './Dashboard';
import About from './About';

export default function App() {
  const dashRef = useRef<HTMLDivElement>(null);
  const [view, setView] = useState<'home' | 'about'>('home');

  const scrollToDash = () => {
    dashRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  if (view === 'about') {
    return <About onBack={() => setView('home')} />;
  }

  return (
    <div className="min-h-screen bg-[--color-surface-0] text-white overflow-x-hidden">
      {/* Fixed overlays */}
      <div className="scanlines" />
      <div className="noise" />

      {/* Hero — full viewport dither section */}
      <Hero onStart={scrollToDash} onAbout={() => setView('about')} />

      {/* Ticker tape separator */}
      <div className="overflow-hidden border-y border-[--color-border] bg-[--color-surface-1] py-2.5">
        <div className="ticker-track inline-flex gap-12 items-center">
          {Array.from({ length: 2 }).map((_, di) =>
            ['FORMULA 1', 'GT3 CHAMPIONSHIP', 'GT4 SERIES', 'WRC RALLY',
              'SPA-FRANCORCHAMPS', 'MONACO', 'SUZUKA', 'SILVERSTONE',
              'MONZA', 'INTERLAGOS', 'RED BULL RING', 'ZANDVOORT'].map((t, i) => (
                <span key={`${di}-${i}`} className="flex items-center gap-12">
                  <span className="font-mono text-[9px] tracking-[0.35em] text-zinc-600">{t}</span>
                  <span className="w-1 h-1 rounded-full bg-[--color-accent] opacity-40 shrink-0" />
                </span>
              ))
          )}
        </div>
      </div>

      {/* Dashboard — predictor section */}
      <div ref={dashRef}>
        <Dashboard />
      </div>
    </div>
  );
}