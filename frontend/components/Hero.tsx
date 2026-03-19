export default function Hero() {
  return (
    <div className="relative overflow-hidden bg-background py-32 px-6 text-center border-b border-cardBorder">
      {/* Background Glowing Orb */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-accent/10 rounded-full blur-[120px] pointer-events-none"></div>
      
      <div className="relative z-10 animate-fade-in">
        <div className="inline-block mb-4 px-4 py-1.5 rounded-full border border-cardBorder bg-card text-accent text-sm font-semibold tracking-wide shadow-glow">
          Next-Generation News Verification
        </div>
        <h1 className="text-5xl md:text-7xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400 mb-6 drop-shadow-sm">
          Fight against fake news
        </h1>
        <p className="text-lg md:text-xl text-gray-400 max-w-2xl mx-auto mb-10 leading-relaxed font-light animate-slide-up">
          CrediNews utilizes state-of-the-art Natural Language Processing to provide 
          instant, highly accurate credibility scores and deep textual analysis.
        </p>
      </div>
    </div>
  )
}
