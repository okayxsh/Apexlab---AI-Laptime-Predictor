import { motion } from 'motion/react';
import { ArrowLeft, Github, ExternalLink } from 'lucide-react';
import Dither from './components/Dither';

interface AboutProps { onBack: () => void; }

const TECH = [
    { label: 'MODEL', value: 'Gradient Boosting Regressor' },
    { label: 'LIBRARY', value: 'scikit-learn' },
    { label: 'SAMPLES', value: '269 lap time records' },
    { label: 'YEARS', value: 'F1 2019–2024' },
    { label: 'CLASSES', value: 'F1 · GT3 · GT4 · Rally' },
    { label: 'MAE', value: '252ms' },
];

export default function About({ onBack }: AboutProps) {
    return (
        <div className="relative min-h-screen flex flex-col overflow-hidden">

            {/* ── Dither background ── */}
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

            {/* Overlays */}
            <div className="absolute inset-0 z-10 bg-gradient-to-b from-black/50 via-black/60 to-black/80" />
            <div className="absolute inset-0 z-10 bg-gradient-to-r from-black/60 via-transparent to-transparent" />
            <div className="scanlines" />
            <div className="noise" />

            {/* ── Nav ── */}
            <motion.header
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.1 }}
                className="relative z-20 flex items-center justify-between px-8 md:px-14 pt-8"
            >
                <div>
                    <div className="flex items-center gap-2.5">
                        <div className="w-2 h-2 rounded-full bg-[--color-accent] animate-glow" />
                        <span className="font-display text-2xl tracking-widest text-white">APEXLAB</span>
                    </div>
                    <p className="font-mono text-[9px] tracking-[0.4em] text-white/30 mt-0.5 ml-[26px]">
                        LAP TIME PREDICTOR
                    </p>
                </div>

                <motion.button
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.3 }}
                    onClick={onBack}
                    className="flex items-center gap-2 font-mono text-[10px] tracking-[0.25em] text-white/50
                     hover:text-white transition-colors duration-200 cursor-pointer group"
                >
                    <ArrowLeft size={13} className="group-hover:-translate-x-0.5 transition-transform" />
                    BACK
                </motion.button>
            </motion.header>

            {/* ── Content ── */}
            <div className="relative z-20 flex-1 flex flex-col justify-center px-8 md:px-14 py-16 max-w-4xl">

                {/* Badge */}
                <motion.div
                    initial={{ opacity: 0, x: -16 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.5, delay: 0.3 }}
                    className="flex items-center gap-2.5 mb-8"
                >
                    <div className="h-px w-6 bg-[--color-accent]" />
                    <span className="font-mono text-[9px] tracking-[0.4em] text-[--color-accent]">
                        ABOUT THE PROJECT
                    </span>
                </motion.div>

                {/* Headline */}
                <div className="overflow-hidden mb-2">
                    <motion.h1
                        initial={{ y: 60 }}
                        animate={{ y: 0 }}
                        transition={{ duration: 0.7, delay: 0.35, ease: [0.16, 1, 0.3, 1] }}
                        className="font-display text-[clamp(3rem,8vw,6.5rem)] leading-[0.92] tracking-wider text-white"
                    >
                        HEY THERE,
                    </motion.h1>
                </div>
                <div className="overflow-hidden mb-10">
                    <motion.h1
                        initial={{ y: 60 }}
                        animate={{ y: 0 }}
                        transition={{ duration: 0.7, delay: 0.45, ease: [0.16, 1, 0.3, 1] }}
                        className="font-display text-[clamp(3rem,8vw,6.5rem)] leading-[0.92] tracking-wider"
                        style={{ WebkitTextStroke: '1px rgba(255,255,255,0.25)', color: 'transparent' }}
                    >
                        I'M YASH.
                    </motion.h1>
                </div>

                {/* Bio */}
                <motion.div
                    initial={{ opacity: 0, y: 16 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.6 }}
                    className="grid grid-cols-1 md:grid-cols-[1fr_320px] gap-10 mb-10"
                >
                    {/* Left — text */}
                    <div className="space-y-5">
                        <p className="text-[15px] text-white/70 leading-relaxed font-light">
                            I'm into the world of racing and I built this predictor to show me what lap times
                            would look like on some of my favorite tracks. You can choose from{' '}
                            <span className="text-white font-medium">F1, GT3, GT4 &amp; Rally</span> for now,
                            and later on I'd be adding a few more cars for fun.
                        </p>

                        <p className="text-[15px] text-white/70 leading-relaxed font-light">
                            How does it actually predict the times? It uses a{' '}
                            <span className="text-[--color-accent] font-medium">Gradient Boosting Regressor</span>{' '}
                            from scikit-learn, trained on 269 real lap time records from F1 (2019–2024),
                            GT3, and GT4 races pulled from actual timing data.
                        </p>

                        <p className="text-[15px] text-white/70 leading-relaxed font-light">
                            If you download the project, you can run it inside your terminal too — all the
                            cars and tracks are the same.
                        </p>

                        <p className="text-[15px] text-white/70 leading-relaxed font-light">
                            In the future I'd work on refining the UI and making the lap time predictions
                            more accurate. Stay tuned!
                        </p>

                        {/* GitHub CTA */}
                        <motion.a
                            href="https://github.com/okayxsh"
                            target="_blank"
                            rel="noopener noreferrer"
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                            className="inline-flex items-center gap-3 mt-2
                         border border-[--color-border] hover:border-[--color-accent]/50
                         bg-[--color-surface-1]/60 hover:bg-[--color-surface-2]/60
                         backdrop-blur-sm px-5 py-3
                         font-mono text-[10px] tracking-[0.25em] text-white/70 hover:text-white
                         transition-all duration-200 cursor-pointer group"
                        >
                            <Github size={13} className="group-hover:text-[--color-accent] transition-colors" />
                            GITHUB — OKAYXSH
                            <ExternalLink size={11} className="text-white/30 group-hover:text-white/60 transition-colors" />
                        </motion.a>
                    </div>

                    {/* Right — tech specs */}
                    <div className="border border-[--color-border] bg-black/30 backdrop-blur-sm">
                        <div className="border-b border-[--color-border] px-5 py-3">
                            <span className="font-mono text-[9px] tracking-[0.35em] text-zinc-500">TECH SPECS</span>
                        </div>
                        <div className="px-5 py-4 space-y-3">
                            {TECH.map(({ label, value }) => (
                                <div key={label} className="flex items-start justify-between gap-4">
                                    <span className="font-mono text-[9px] tracking-[0.2em] text-zinc-600 shrink-0">{label}</span>
                                    <span className="font-mono text-[11px] text-zinc-300 text-right">{value}</span>
                                </div>
                            ))}
                        </div>
                        <div className="border-t border-[--color-border] px-5 py-3">
                            <p className="font-mono text-[8px] tracking-[0.2em] text-zinc-700">
                                TERMINAL VERSION AVAILABLE ON GITHUB
                            </p>
                        </div>
                    </div>
                </motion.div>
            </div>

            {/* ── Bottom bar ── */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.9 }}
                className="relative z-20 border-t border-white/[0.06] bg-black/30 backdrop-blur-sm
                   px-8 md:px-14 py-4 flex items-center justify-between"
            >
                <span className="font-mono text-[8px] tracking-[0.3em] text-white/20">APEXLAB © 2025</span>
                <div className="flex items-center gap-6">
                    {['F1', 'GT3', 'GT4', 'WRC'].map(cat => (
                        <span key={cat} className="font-mono text-[9px] tracking-[0.2em] text-white/25">
                            {cat}
                        </span>
                    ))}
                </div>
            </motion.div>
        </div>
    );
}