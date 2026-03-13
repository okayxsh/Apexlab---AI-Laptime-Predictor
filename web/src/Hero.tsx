import { useRef } from 'react';
import { motion } from 'motion/react';
import { ChevronDown } from 'lucide-react';
import Dither from './components/Dither';

interface HeroProps { onStart: () => void; }

const STATS = [
  { value: '59', label: 'Circuits' },
  { value: '20', label: 'Vehicles' },
  { value: '252ms', label: 'Model MAE' },
  { value: '94%', label: 'Accuracy' },
];

export default function Hero({ onStart }: HeroProps) {
  return (
    <section className="relative w-full h-screen flex flex-col overflow-hidden">

      {/* ── Dither background — full bleed ── */}
      <div className="absolute inset-0 z-0">
        <Dither
          waveColor={[0.55, 0, 0.05]}
          disableAnimation={false}
          enableMouseInteraction
          mouseRadius={0.3}
          colorNum={4}
          waveAmplitude={0.34}
          waveFrequency={3}
          waveSpeed={0.02}
        />
      </div>

      {/* Dark gradient overlay — bottom fade so content reads */}
      <div className="absolute inset-0 z-10 bg-gradient-to-b from-black/40 via-transparent to-[--color-surface-0]" />
      {/* Left vignette */}
      <div className="absolute inset-0 z-10 bg-gradient-to-r from-black/60 via-transparent to-transparent" />

      {/* ── Nav bar ─────────────────────────── */}
      <motion.header
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.2 }}
        className="relative z-20 flex items-center justify-between px-8 md:px-14 pt-8"
      >
        <div>
          <div className="flex items-center gap-2.5">
            <div className="w-2 h-2 rounded-full bg-[--color-accent] animate-glow" />
            <span className="font-display text-2xl tracking-widest text-white">
              LAPTIME
            </span>
          </div>
          <p className="font-mono text-[9px] tracking-[0.4em] text-white/30 mt-0.5 ml-[26px]">
            PREDICTOR ENGINE
          </p>
        </div>

        <div className="flex items-center gap-6">
          {['F1', 'GT3', 'GT4', 'WRC'].map((cat) => (
            <span key={cat} className="font-mono text-[10px] tracking-[0.25em] text-white/40 hover:text-white/70 transition-colors cursor-default">
              {cat}
            </span>
          ))}
        </div>
      </motion.header>

      {/* ── Hero content ────────────────────── */}
      <div className="relative z-20 flex-1 flex flex-col justify-center px-8 md:px-14 pb-16">

        {/* Badge */}
        <motion.div
          initial={{ opacity: 0, x: -16 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5, delay: 0.5 }}
          className="flex items-center gap-2.5 mb-6"
        >
          <div className="h-px w-6 bg-[--color-accent]" />
          <span className="font-mono text-[9px] tracking-[0.4em] text-[--color-accent]">
            ML-POWERED RACING ANALYTICS
          </span>
        </motion.div>

        {/* Main headline */}
        <div className="overflow-hidden mb-3">
          <motion.h1
            initial={{ y: 80 }}
            animate={{ y: 0 }}
            transition={{ duration: 0.75, delay: 0.55, ease: [0.16, 1, 0.3, 1] }}
            className="font-display text-[clamp(4rem,11vw,9rem)] leading-[0.92] tracking-wider text-white"
          >
            PREDICT
          </motion.h1>
        </div>
        <div className="overflow-hidden mb-6">
          <motion.h1
            initial={{ y: 80 }}
            animate={{ y: 0 }}
            transition={{ duration: 0.75, delay: 0.65, ease: [0.16, 1, 0.3, 1] }}
            className="font-display text-[clamp(4rem,11vw,9rem)] leading-[0.92] tracking-wider"
            style={{ WebkitTextStroke: '1px rgba(255,255,255,0.25)', color: 'transparent' }}
          >
            LAP TIMES
          </motion.h1>
        </div>

        {/* Sub */}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.6, delay: 0.9 }}
          className="text-[15px] text-white/45 max-w-md leading-relaxed mb-10 font-light"
        >
          Gradient-boosted ML model trained on 269 real race samples.
          Sector splits, top speeds, and confidence scoring across
          F1, GT3, GT4 and WRC categories.
        </motion.p>

        {/* CTA */}
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 1.05 }}
          className="flex items-center gap-4"
        >
          <button
            onClick={onStart}
            className="group flex items-center gap-3 bg-[--color-accent] hover:bg-[--color-accent-soft]
                       px-7 py-3.5 text-white font-mono text-[11px] tracking-[0.25em]
                       transition-all duration-200 cursor-pointer
                       shadow-[0_0_40px_var(--color-accent-glow)]
                       hover:shadow-[0_0_60px_var(--color-accent-glow)]"
          >
            RUN PREDICTION
            <ChevronDown size={13} className="group-hover:translate-y-0.5 transition-transform" />
          </button>

          <div className="h-px w-12 bg-white/20" />

          <span className="font-mono text-[9px] tracking-[0.3em] text-white/30">
            SCROLL TO DASHBOARD
          </span>
        </motion.div>
      </div>

      {/* ── Stats strip — bottom ─────────────── */}
      <motion.div
        initial={{ opacity: 0, y: 16 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 1.2 }}
        className="relative z-20 flex items-stretch border-t border-white/[0.06] bg-black/30 backdrop-blur-sm"
      >
        {STATS.map((s, i) => (
          <div
            key={s.label}
            className={`flex-1 px-8 py-5 ${i < STATS.length - 1 ? 'border-r border-white/[0.06]' : ''}`}
          >
            <p className="font-display text-3xl text-white tracking-wider mb-0.5">{s.value}</p>
            <p className="font-mono text-[9px] tracking-[0.3em] text-white/30">{s.label.toUpperCase()}</p>
          </div>
        ))}
      </motion.div>
    </section>
  );
}
