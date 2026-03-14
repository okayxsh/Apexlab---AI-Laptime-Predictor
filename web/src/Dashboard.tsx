import { motion, useInView } from 'motion/react';
import { Play, Zap, Wind, Shield, ChevronRight } from 'lucide-react';
import { useState, useEffect, useRef } from 'react';
import { predict, TRACKS, CARS, getAsciiMap } from './predictor';
import type { PredictionResult } from './predictor';

/* ── Types ─────────────────────────────────── */
interface Track { id: string; name: string; }
interface Car { id: string; name: string; }

/* ── Typing animation ──────────────────────── */
function TypedTime({ time, delay = 0 }: { time: string; delay?: number }) {
  const [displayed, setDisplayed] = useState('');
  const [done, setDone] = useState(false);
  useEffect(() => {
    setDisplayed('');
    setDone(false);
    const t = setTimeout(() => {
      let i = 0;
      const iv = setInterval(() => {
        setDisplayed(time.slice(0, i + 1));
        i++;
        if (i >= time.length) { clearInterval(iv); setDone(true); }
      }, 75);
      return () => clearInterval(iv);
    }, delay);
    return () => clearTimeout(t);
  }, [time, delay]);

  return (
    <span>
      {displayed}
      {!done && (
        <span className="inline-block w-[2px] h-[0.8em] bg-[--color-accent] ml-0.5 animate-blink align-baseline" />
      )}
    </span>
  );
}

/* ── Field ─────────────────────────────────── */
function Field({ label, options, value, onChange, delay, disabled = false }: {
  label: string;
  options: { id: string; name: string }[];
  value: string;
  onChange: (v: string) => void;
  delay: number;
  disabled?: boolean;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay }}
    >
      <label className="block font-mono text-[9px] tracking-[0.35em] text-zinc-600 mb-2">
        {label}
      </label>
      <div className="relative">
        <select
          value={value}
          onChange={e => onChange(e.target.value)}
          disabled={disabled}
          className="w-full bg-[--color-surface-2] border border-[--color-border]
                     hover:border-[--color-border-hover] focus:border-[--color-accent]/40
                     pl-3 pr-8 py-2.5 text-[12px] text-white/80 font-mono
                     outline-none transition-all duration-200 cursor-pointer
                     disabled:opacity-40 disabled:cursor-not-allowed"
        >
          {options.map(o => <option key={o.id} value={o.id}>{o.name}</option>)}
        </select>
      </div>
    </motion.div>
  );
}

/* ── Section label ─────────────────────────── */
function SectionLabel({ text }: { text: string }) {
  return (
    <div className="flex items-center gap-4 mb-10">
      <div className="h-px w-8 bg-[--color-accent]" />
      <span className="font-mono text-[9px] tracking-[0.4em] text-[--color-accent]">{text}</span>
      <div className="h-px flex-1 bg-[--color-border]" />
    </div>
  );
}

/* ── ASCII Track Map ───────────────────────── */
function AsciiMap({ trackId, trackName, category }: { trackId: string; trackName: string; category: string }) {
  const map = getAsciiMap(trackId);
  const td = TRACKS[category]?.find(t => t.id === trackId);

  return (
    <div className="border border-[--color-border] bg-[--color-surface-1] flex flex-col flex-1">
      {/* Header */}
      <div className="border-b border-[--color-border] px-5 py-3 flex items-center justify-between shrink-0">
        <span className="font-mono text-[9px] tracking-[0.35em] text-zinc-600">CIRCUIT MAP</span>
        <span className="font-mono text-[8px] tracking-[0.2em] text-zinc-700 uppercase truncate max-w-[200px]">
          {trackName}
        </span>
      </div>

      {/* ASCII art */}
      <div className="flex-1 overflow-auto p-4 min-h-[300px]">
        <pre
          className="font-mono leading-[1.2] text-[--color-accent]/35
                     hover:text-[--color-accent]/55 transition-colors duration-500
                     whitespace-pre select-none"
          style={{ fontSize: 'clamp(4px, 0.55vw, 6.5px)' }}
        >
          {map}
        </pre>
      </div>

      {/* Track stats strip */}
      <div className="border-t border-[--color-border] bg-[--color-surface-2] px-5 py-3 grid grid-cols-3 gap-4 shrink-0">
        {[
          ['LENGTH', td ? `${(td as any).length_km} km` : '—'],
          ['CORNERS', td ? `${(td as any).corners ?? '—'}` : '—'],
          ['SURFACE', td ? `${((td as any).surface ?? 'tarmac').toUpperCase()}` : '—'],
        ].map(([k, v]) => (
          <div key={k}>
            <p className="font-mono text-[7px] tracking-[0.3em] text-zinc-700 mb-0.5">{k}</p>
            <p className="font-mono text-[11px] text-zinc-400">{v}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

/* ── Categories ────────────────────────────── */
const CATEGORIES = [
  { id: 'f1', name: 'Formula 1' },
  { id: 'gt3', name: 'GT3' },
  { id: 'gt4', name: 'GT4' },
  { id: 'rally', name: 'Rally' },
];

const CONDITIONS = [
  { id: 'dry', name: 'Dry' },
  { id: 'wet', name: 'Wet' },
  { id: 'damp', name: 'Damp' },
];

/* ── Split time for display ────────────────── */
function splitTime(formatted: string) {
  const dotIdx = formatted.indexOf('.');
  if (dotIdx === -1) return { main: formatted, decimal: '' };
  return {
    main: formatted.slice(0, dotIdx),
    decimal: formatted.slice(dotIdx),
  };
}

export default function Dashboard() {
  const ref = useRef<HTMLDivElement>(null);
  const inView = useInView(ref, { once: true, margin: '-80px' });

  const [category, setCategory] = useState('f1');
  const [tracks, setTracks] = useState<Track[]>([]);
  const [cars, setCars] = useState<Car[]>([]);
  const [track, setTrack] = useState('');
  const [car, setCar] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PredictionResult | null>(null);
  const [error, setError] = useState('');

  /* Load tracks + cars when category changes */
  useEffect(() => {
    setResult(null);
    setError('');
    const t = TRACKS[category] ?? [];
    const c = CARS[category] ?? [];
    setTracks(t.map(x => ({ id: x.id, name: x.name })));
    setCars(c.map(x => ({ id: x.id, name: x.name })));
    setTrack(t[0]?.id ?? '');
    setCar(c[0]?.id ?? '');
  }, [category]);

  /* Run prediction */
  const handlePredict = () => {
    if (!track || !car) return;
    setLoading(true);
    setResult(null);
    setError('');

    setTimeout(() => {
      const res = predict(category, track, car);
      if ('error' in res) {
        setError(res.error);
      } else {
        setResult(res);
      }
      setLoading(false);
    }, 800);
  };

  /* Derived display values */
  const isRally = result && 'is_rally' in result && result.is_rally === true;

  const timeFormatted = isRally
    ? (result as any).stage_time_formatted ?? ''
    : (result as any)?.lap_time_formatted ?? '';

  const { main: timeMain, decimal: timeDec } = splitTime(timeFormatted);

  const sectors = isRally
    ? [
      { label: 'SS1', time: (result as any).ss1_formatted ?? '-', color: 'bg-emerald-500', width: '65%' },
      { label: 'SS2', time: (result as any).ss2_formatted ?? '-', color: 'bg-amber-500', width: '82%' },
      { label: 'SS3', time: (result as any).ss3_formatted ?? '-', color: 'bg-sky-400', width: '54%' },
    ]
    : [
      { label: 'SECTOR 1', time: (result as any)?.sector_1_formatted ?? '-', color: 'bg-emerald-500', width: '72%' },
      { label: 'SECTOR 2', time: (result as any)?.sector_2_formatted ?? '-', color: 'bg-amber-500', width: '91%' },
      { label: 'SECTOR 3', time: (result as any)?.sector_3_formatted ?? '-', color: 'bg-sky-400', width: '58%' },
    ];

  const carName = result ? (result as any).car_name ?? car : '';
  const trackName = tracks.find(t => t.id === track)?.name ?? '—';

  return (
    <section ref={ref} className="min-h-screen bg-[--color-surface-0] px-8 md:px-14 py-20">

      <SectionLabel text="PREDICTION DASHBOARD" />

      {/* ── 3-column grid ── */}
      <div className="grid grid-cols-1 lg:grid-cols-[300px_1fr_1fr] gap-6 max-w-7xl">

        {/* ═══ COL 1 — Config ═══════════════════ */}
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={inView ? { opacity: 1, x: 0 } : {}}
          transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
          className="flex flex-col"
        >
          <div className="border border-[--color-border] bg-[--color-surface-1] p-5 mb-px">
            <div className="flex items-center justify-between">
              <span className="font-mono text-[9px] tracking-[0.35em] text-zinc-600">CONFIGURATION</span>
              <div className="flex items-center gap-1.5">
                <div className={`w-1.5 h-1.5 rounded-full transition-colors ${result ? 'bg-emerald-500' : 'bg-zinc-700'}`} />
                <span className="font-mono text-[8px] tracking-[0.2em] text-zinc-700">
                  {result ? 'COMPLETE' : 'STANDBY'}
                </span>
              </div>
            </div>
          </div>

          <div className="border border-t-0 border-[--color-border] bg-[--color-surface-1] p-5 space-y-4 flex-1">
            <Field label="CATEGORY" options={CATEGORIES} value={category} onChange={setCategory} delay={0.1} />
            <Field label="CIRCUIT" options={tracks} value={track} onChange={setTrack} delay={0.15} />
            <Field label="VEHICLE" options={cars} value={car} onChange={setCar} delay={0.2} />
            <Field label="CONDITIONS" options={CONDITIONS} value="dry" onChange={() => { }} delay={0.25} />

            <div className="h-px bg-[--color-border] my-2" />

            <motion.button
              initial={{ opacity: 0 }}
              animate={inView ? { opacity: 1 } : {}}
              transition={{ delay: 0.35 }}
              whileHover={{ scale: 1.01 }}
              whileTap={{ scale: 0.98 }}
              onClick={handlePredict}
              disabled={loading || !track || !car}
              className="w-full flex items-center justify-center gap-2.5
                         bg-[--color-accent] hover:bg-[--color-accent-soft]
                         disabled:opacity-40 disabled:cursor-not-allowed
                         text-white font-mono text-[10px] tracking-[0.3em]
                         py-3.5 transition-all duration-200 cursor-pointer
                         shadow-[0_0_30px_var(--color-accent-glow)]
                         hover:shadow-[0_0_50px_var(--color-accent-glow)]"
            >
              {loading ? (
                <>
                  <span className="w-3 h-3 border border-white/30 border-t-white rounded-full animate-spin" />
                  COMPUTING
                </>
              ) : (
                <>
                  <Play size={11} fill="currentColor" />
                  RUN PREDICTION
                  <ChevronRight size={11} />
                </>
              )}
            </motion.button>

            {error && (
              <p className="font-mono text-[9px] text-red-500 tracking-wide text-center">{error}</p>
            )}
          </div>

          <div className="border border-t-0 border-[--color-border] bg-[--color-surface-2] px-5 py-4">
            <p className="font-mono text-[8px] tracking-[0.25em] text-zinc-700 mb-2">MODEL INFO</p>
            <div className="space-y-1.5">
              {[
                ['ALGORITHM', 'Gradient Boosting'],
                ['SAMPLES', '269 race records'],
                ['MAE', '252ms'],
                ['FEATURES', '9 inputs'],
              ].map(([k, v]) => (
                <div key={k} className="flex items-center justify-between">
                  <span className="font-mono text-[8px] text-zinc-700">{k}</span>
                  <span className="font-mono text-[9px] text-zinc-500">{v}</span>
                </div>
              ))}
            </div>
          </div>
        </motion.div>

        {/* ═══ COL 2 — ASCII Track Map ══════════ */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={inView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
          className="flex flex-col"
        >
          <div className="border border-[--color-border] bg-[--color-surface-1] p-5 mb-px shrink-0">
            <span className="font-mono text-[9px] tracking-[0.35em] text-zinc-600">CIRCUIT OVERVIEW</span>
          </div>
          <AsciiMap trackId={track} trackName={trackName} category={category} />
        </motion.div>

        {/* ═══ COL 3 — Prediction Output ════════ */}
        <motion.div
          initial={{ opacity: 0, x: 20 }}
          animate={inView ? { opacity: 1, x: 0 } : {}}
          transition={{ duration: 0.6, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
          className="flex flex-col"
        >
          <div className="border border-[--color-border] bg-[--color-surface-1] px-6 py-5 mb-px flex items-center justify-between">
            <span className="font-mono text-[9px] tracking-[0.35em] text-zinc-600">PREDICTION OUTPUT</span>
            <span className="font-mono text-[8px] tracking-[0.2em] text-zinc-700 uppercase">
              {CATEGORIES.find(c => c.id === category)?.name} · {trackName}
            </span>
          </div>

          <div className="border border-t-0 border-[--color-border] bg-[--color-surface-1] flex-1 flex flex-col min-h-[500px]">

            {/* Empty state */}
            {!result && !loading && !error && (
              <div className="flex-1 flex flex-col items-center justify-center gap-3 text-center p-8">
                <div className="w-px h-16 bg-gradient-to-b from-transparent via-[--color-border-hover] to-transparent mb-4" />
                <p className="font-mono text-[10px] tracking-[0.3em] text-zinc-700">AWAITING INPUT</p>
                <p className="text-zinc-600 text-sm font-light max-w-xs">
                  Configure parameters and run a prediction
                </p>
                <div className="w-px h-16 bg-gradient-to-b from-transparent via-[--color-border-hover] to-transparent mt-4" />
              </div>
            )}

            {/* Loading */}
            {loading && (
              <div className="flex-1 flex flex-col items-center justify-center gap-4 p-8">
                <div className="flex gap-1.5">
                  {[0, 1, 2, 3, 4].map(i => (
                    <motion.div
                      key={i}
                      animate={{ scaleY: [1, 2.5, 1] }}
                      transition={{ duration: 0.6, delay: i * 0.1, repeat: Infinity }}
                      className="w-[3px] h-5 bg-[--color-accent] origin-bottom"
                    />
                  ))}
                </div>
                <p className="font-mono text-[9px] tracking-[0.35em] text-zinc-700 animate-pulse">
                  RUNNING MODEL
                </p>
              </div>
            )}

            {/* Error */}
            {error && !loading && (
              <div className="flex-1 flex items-center justify-center p-8">
                <p className="font-mono text-[10px] text-red-500 tracking-wide text-center">{error}</p>
              </div>
            )}

            {/* Results */}
            {result && !loading && (
              <motion.div
                key={timeFormatted}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 0.4 }}
                className="flex-1 flex flex-col p-6"
              >
                <div className="mb-6">
                  <p className="font-mono text-[10px] tracking-[0.3em] text-zinc-400 mb-3">
                    {isRally ? 'PREDICTED STAGE TIME' : 'PREDICTED LAP TIME'}
                  </p>
                  <div className="flex items-end gap-2">
                    <span className="font-display text-[clamp(3rem,6vw,5rem)] leading-none text-white tracking-wider">
                      <TypedTime time={timeMain} delay={100} />
                    </span>
                    {timeDec && (
                      <span className="font-display text-[clamp(2rem,4vw,3.2rem)] leading-none text-[--color-accent] tracking-wider mb-1">
                        <TypedTime time={timeDec} delay={500} />
                      </span>
                    )}
                  </div>
                  <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 1.2 }}
                    className="flex items-center gap-3 mt-2"
                  >
                    <div className="h-px w-6 bg-[--color-accent]/40" />
                    <span className="font-mono text-[11px] tracking-[0.15em] text-zinc-300">
                      {carName} · {trackName} · Dry
                    </span>
                  </motion.div>
                </div>

                {/* Sectors */}
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 1.4 }}
                  className="grid grid-cols-3 gap-2 mb-5"
                >
                  {sectors.map((s, i) => (
                    <div key={s.label} className="border border-[--color-border] bg-[--color-surface-2] p-3">
                      <p className="font-mono text-[10px] tracking-[0.2em] text-zinc-400 mb-1.5">{s.label}</p>
                      <p className="font-mono text-sm font-semibold text-white tabular-nums mb-2">{s.time}</p>
                      <div className="h-[2px] bg-[--color-surface-0]">
                        <motion.div
                          initial={{ width: 0 }}
                          animate={{ width: s.width }}
                          transition={{ delay: 1.6 + i * 0.12, duration: 0.7, ease: 'easeOut' }}
                          className={`h-full ${s.color}`}
                        />
                      </div>
                    </div>
                  ))}
                </motion.div>

                {/* Telemetry */}
                <motion.div
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ delay: 2.0 }}
                  className="border border-[--color-border] bg-[--color-surface-2] grid grid-cols-3"
                >
                  {[
                    { icon: Zap, label: 'TOP SPEED', value: `${result.top_speed_kmh} km/h` },
                    { icon: Wind, label: 'AVG SPEED', value: `${result.avg_speed_kmh} km/h` },
                    { icon: Shield, label: 'CONFIDENCE', value: result.confidence.split(' ')[0] },
                  ].map((s, i) => (
                    <div key={s.label} className={`flex items-center gap-2 px-4 py-3 ${i < 2 ? 'border-r border-[--color-border]' : ''}`}>
                      <s.icon size={12} className="text-[--color-accent]/60 shrink-0" />
                      <div>
                        <p className="font-mono text-[10px] tracking-[0.2em] text-zinc-400 mb-0.5">{s.label}</p>
                        <p className="font-mono text-[13px] text-white font-semibold">{s.value}</p>
                      </div>
                    </div>
                  ))}
                </motion.div>
              </motion.div>
            )}
          </div>
        </motion.div>
      </div>

      {/* Bottom row */}
      <motion.div
        initial={{ opacity: 0, y: 12 }}
        animate={inView ? { opacity: 1, y: 0 } : {}}
        transition={{ duration: 0.5, delay: 0.5 }}
        className="flex items-center gap-4 mt-8 max-w-7xl"
      >
        <span className="font-mono text-[8px] tracking-[0.35em] text-zinc-800 shrink-0">SUPPORTED CATEGORIES</span>
        <div className="h-px flex-1 bg-[--color-border]" />
        {['Formula 1', 'GT3 Championship', 'GT4 Series', 'WRC Rally'].map(c => (
          <span key={c} className="font-mono text-[9px] tracking-[0.15em] text-zinc-700
                                    border border-[--color-border] px-3 py-1.5
                                    hover:border-[--color-border-hover] hover:text-zinc-500
                                    transition-all cursor-default">
            {c}
          </span>
        ))}
      </motion.div>
    </section>
  );
}