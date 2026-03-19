'use client';
import { useState, useRef, MouseEvent } from 'react';
import axios from 'axios';

export default function CheckNews() {
  const [text, setText] = useState('');
  const [model, setModel] = useState('Logistic Regression');
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  
  const cardRef = useRef<HTMLDivElement>(null);
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (e: MouseEvent<HTMLDivElement>) => {
    if (!cardRef.current) return;
    const rect = cardRef.current.getBoundingClientRect();
    setMousePosition({
      x: e.clientX - rect.left,
      y: e.clientY - rect.top,
    });
  };

  const wordCount = text.trim() ? text.trim().split(/\s+/).length : 0;

  const handleCheck = async () => {
    if (text.length < 20) {
      setError('Please enter at least 20 characters.');
      return;
    }
    setError('');
    setLoading(true);
    setResult(null); // Clear previous result for shimmer effect
    try {
      const apiUrl = 'https://credinews-n950.onrender.com';
      const res = await axios.post(`${apiUrl}/predict`, {
        text,
        model_name: model
      });
      setResult(res.data);
      
      const history = JSON.parse(localStorage.getItem('credinews_history') || '[]');
      history.unshift({ text: text.substring(0, 50) + '...', prediction: res.data.prediction, date: new Date().toISOString() });
      if (history.length > 10) history.pop();
      localStorage.setItem('credinews_history', JSON.stringify(history));
    } catch (err: any) {
      setError(err.response?.data?.detail || 'An error occurred connecting to the API.');
    } finally {
      setLoading(false);
    }
  }

  // Highlight words from explanation in original text
  const renderHighlightedText = () => {
    if (!result || !result.explanation || result.explanation[0] === "No significant words found") {
      return <p className="text-gray-300 leading-relaxed max-h-[300px] overflow-y-auto pr-4 whitespace-pre-wrap">{text}</p>;
    }
    
    let highlightedHTML = text;
    // Sort by length descending so longer phrases match first
    const sortedTerms = [...result.explanation].sort((a, b) => b.length - a.length);
    const highlightColor = result.prediction === 'REAL' ? 'bg-green-500/20 text-green-300 border-green-500/40 shadow-[0_0_10px_rgba(34,197,94,0.3)]' : 'bg-red-500/20 text-red-300 border-red-500/40 shadow-[0_0_10px_rgba(239,68,68,0.3)]';

    sortedTerms.forEach(term => {
      const escapedTerm = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      // Create unique temporary tags that won't appear in normal text
      const regex = new RegExp(`(${escapedTerm})`, 'gi');
      highlightedHTML = highlightedHTML.replace(regex, `!|!$1|!|`);
    });

    const parts = highlightedHTML.split(/!\|!|\|!\|/g);
    
    return (
      <div className="text-gray-300 leading-relaxed max-h-[300px] overflow-y-auto pr-4 whitespace-pre-wrap custom-scrollbar">
        {parts.map((part, i) => {
          const isHighlighted = sortedTerms.some(t => t.toLowerCase() === part.toLowerCase());
          return isHighlighted ? (
            <span key={i} className={`px-1.5 py-0.5 rounded border ${highlightColor} font-semibold mx-0.5 transition-all duration-300 hover:brightness-125`}>
              {part}
            </span>
          ) : (
            <span key={i}>{part}</span>
          );
        })}
      </div>
    );
  };

  return (
    <div className="max-w-5xl mx-auto py-16 px-6 animate-fade-in relative">
      <div className="text-center mb-12">
        <h1 className="text-5xl md:text-6xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400 drop-shadow-sm tracking-tight mb-4">
          Deep Fake Analysis
        </h1>
        <p className="text-gray-400 text-lg md:text-xl font-light">Input your content below. Our neural networks will scan patterns and linguisitics to detect deception.</p>
      </div>
      
      <div 
        ref={cardRef}
        onMouseMove={handleMouseMove}
        className="bg-card backdrop-blur-xl p-8 rounded-3xl shadow-2xl mb-12 border border-cardBorder transition-colors duration-300 relative overflow-hidden group"
      >
        {/* Dynamic Cursor-tracking Glow inside card */}
        <div 
          className="absolute pointer-events-none rounded-full blur-[100px] bg-accent/20 w-[600px] h-[600px] transition-opacity duration-500 opacity-0 group-hover:opacity-100"
          style={{
            left: `${mousePosition.x - 300}px`,
            top: `${mousePosition.y - 300}px`,
          }}
        ></div>
        
        <div className="flex justify-between items-center mb-8 relative z-10">
          <label className="text-sm font-bold text-gray-400 uppercase tracking-widest flex items-center gap-2">
            <svg className="w-5 h-5 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" /></svg>
            Select AI Engine
          </label>
          <div className="relative group/select">
            <select 
              value={model} 
              onChange={(e) => setModel(e.target.value)}
              className="appearance-none bg-[#0B152A] border border-cardBorder hover:border-accent/50 rounded-xl pl-5 pr-12 py-3 text-sm font-semibold text-white focus:outline-none focus:border-accent focus:ring-1 focus:ring-accent transition-all cursor-pointer shadow-none group-hover/select:shadow-[0_0_15px_rgba(249,115,22,0.15)]"
            >
              <option>Logistic Regression</option>
              <option>Multinomial Naive Bayes</option>
              <option>Random Forest</option>
            </select>
            <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-4 text-accent">
              <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
            </div>
          </div>
        </div>
        
        <div className="relative z-10">
          <textarea
            className="w-full bg-[#050A14]/70 border border-cardBorder rounded-2xl p-6 text-white focus:border-accent focus:ring-1 focus:ring-accent focus:outline-none min-h-[260px] mb-4 text-lg leading-relaxed placeholder-gray-600 transition-all resize-y shadow-inner group-hover:bg-[#050A14]/90"
            placeholder="Paste news headline or full article text here..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <div className="flex justify-between text-xs font-bold text-gray-500 mb-8 px-2 uppercase tracking-wide">
            <span>{text.length} characters</span>
            <span>{wordCount} words</span>
          </div>
          
          {error && (
            <div className="bg-red-500/10 border border-red-500/30 text-red-400 text-sm font-bold mb-8 p-5 rounded-xl flex items-center gap-3 animate-fade-in shadow-lg">
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>
              {error}
            </div>
          )}
          
          <button 
            onClick={handleCheck}
            disabled={loading}
            className="w-full bg-gradient-to-r from-accent to-orange-500 hover:from-orange-500 hover:to-orange-400 text-white font-extrabold py-5 px-6 rounded-2xl shadow-glow hover:shadow-glow-green transform hover:-translate-y-1 transition-all duration-300 disabled:opacity-50 disabled:transform-none disabled:shadow-none disabled:cursor-wait flex justify-center items-center gap-3 text-xl tracking-wide group/btn overflow-hidden relative"
          >
            {/* Button inner shine effect */}
            <div className="absolute inset-0 -translate-x-full group-hover/btn:animate-[shimmer_1.5s_infinite] bg-gradient-to-r from-transparent via-white/20 to-transparent skew-x-12"></div>
            
            {loading ? (
              <>
                <svg className="animate-spin -ml-1 mr-3 h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle><path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                AI Processing...
              </>
            ) : 'Analyze Credibility'}
          </button>
        </div>
      </div>

      {loading && !result && (
        <div className="bg-card backdrop-blur-md p-10 rounded-3xl shadow-2xl border border-cardBorder animate-pulse-slow relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent animate-shimmer bg-[200%_100%]"></div>
          <div className="h-8 bg-[#0B152A] rounded-full w-1/3 mb-10"></div>
          <div className="flex gap-8 mb-8">
            <div className="w-32 h-32 bg-[#0B152A] rounded-2xl"></div>
            <div className="flex-1 space-y-4 py-2">
              <div className="h-6 bg-[#0B152A] rounded-full w-1/4"></div>
              <div className="h-4 bg-[#0B152A] rounded-full w-full"></div>
            </div>
          </div>
          <div className="h-32 bg-[#0B152A] rounded-xl w-full"></div>
        </div>
      )}

      {result && !loading && (
        <div className="bg-gradient-to-br from-card to-[#0B152A] backdrop-blur-xl p-10 rounded-3xl shadow-2xl border border-cardBorder animate-slide-up relative overflow-hidden">
          {/* Result Background Glow */}
          <div className={`absolute top-0 right-0 w-[600px] h-[600px] rounded-full blur-[150px] pointer-events-none opacity-[0.15] transform translate-x-1/2 -translate-y-1/2 ${result.prediction === 'REAL' ? 'bg-green-500' : 'bg-red-500'}`}></div>

          <div className="relative z-10">
            <h2 className="text-2xl font-extrabold text-white mb-8 border-b border-cardBorder pb-6 flex items-center gap-3">
              <svg className="w-7 h-7 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
              Final Analysis Report
            </h2>
            
            <div className="flex flex-col md:flex-row items-start md:items-center gap-10 mb-10">
              <div className={`text-5xl font-black px-10 py-6 rounded-3xl border-2 flex flex-col items-center justify-center ${
                result.prediction === 'REAL' 
                  ? 'bg-green-500/10 text-green-400 border-green-500/40 shadow-[0_0_40px_rgba(34,197,94,0.25)]' 
                  : 'bg-red-500/10 text-red-500 border-red-500/40 shadow-[0_0_40px_rgba(239,68,68,0.25)]'
              }`}>
                {result.prediction}
                <span className={`text-sm font-bold mt-2 tracking-widest uppercase ${result.prediction === 'REAL' ? 'text-green-500/70' : 'text-red-500/70'}`}>
                  Prediction
                </span>
              </div>
              
              <div className="flex-1 w-full bg-[#050A14]/50 p-6 rounded-2xl border border-cardBorder">
                <div className="flex justify-between items-end mb-4">
                  <span className="text-sm font-bold text-gray-400 uppercase tracking-widest flex items-center gap-2">
                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" /></svg>
                    AI Confidence
                  </span>
                  <span className="text-4xl font-black text-white">{result.confidence.toFixed(1)}%</span>
                </div>
                <div className="w-full bg-[#0B152A] rounded-full h-4 shadow-inner overflow-hidden border border-cardBorder">
                  <div 
                    className={`h-full rounded-full transition-all duration-[1500ms] ease-out relative ${result.prediction === 'REAL' ? 'bg-gradient-to-r from-green-600 to-green-400' : 'bg-gradient-to-r from-red-600 to-red-400'}`} 
                    style={{ width: `${result.confidence}%` }}
                  >
                    <div className="absolute top-0 right-0 bottom-0 w-16 bg-white/30 blur-[4px]"></div>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="bg-[#050A14]/60 rounded-2xl p-8 border border-cardBorder shadow-inner h-full">
                <h3 className="text-sm font-bold text-gray-300 uppercase tracking-widest mb-6 flex items-center gap-2">
                  <svg className="w-5 h-5 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" /></svg>
                  Linguistic Indicators
                </h3>
                <p className="text-sm text-gray-400 mb-6 font-light">The AI isolated these specific n-grams as critical indicators supporting its conclusion:</p>
                <div className="flex flex-wrap gap-3">
                  {result.explanation.map((word: string, i: number) => (
                    <span key={i} className="bg-card border border-cardBorder px-4 py-2 rounded-xl text-sm font-bold text-gray-200 shadow-sm hover:border-accent hover:text-white transition-all transform hover:-translate-y-0.5 cursor-default">
                      {word}
                    </span>
                  ))}
                </div>
              </div>

              <div className="bg-[#050A14]/60 rounded-2xl p-8 border border-cardBorder shadow-inner relative">
                <h3 className="text-sm font-bold text-gray-300 uppercase tracking-widest mb-6 flex items-center gap-2">
                  <svg className="w-5 h-5 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" /></svg>
                  X-Ray Text Inspector
                </h3>
                <p className="text-sm text-gray-400 mb-4 font-light">Visualizing how the AI scanned the input. Highlighted phrases mathematically contributed to the score.</p>
                <div className="bg-[#0B152A]/50 p-5 rounded-xl border border-white/5">
                  {renderHighlightedText()}
                </div>
              </div>
            </div>

          </div>
        </div>
      )}
    </div>
  )
}
