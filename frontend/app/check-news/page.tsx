'use client';
import { useState } from 'react';
import axios from 'axios';

export default function CheckNews() {
  const [text, setText] = useState('');
  const [model, setModel] = useState('Logistic Regression');
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const wordCount = text.trim() ? text.trim().split(/\s+/).length : 0;

  const handleCheck = async () => {
    if (text.length < 20) {
      setError('Please enter at least 20 characters.');
      return;
    }
    setError('');
    setLoading(true);
    try {
      const apiUrl = 'https://credinews-n950.onrender.com';
      const res = await axios.post(`${apiUrl}/predict`, {
        text,
        model_name: model
      });
      setResult(res.data);
      
      // Save to local storage history
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

  return (
    <div className="max-w-4xl mx-auto py-16 px-6 animate-fade-in">
      <div className="text-center mb-10">
        <h1 className="text-4xl md:text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-300 drop-shadow-sm tracking-tight mb-3">
          AI Credibility Analysis
        </h1>
        <p className="text-gray-400 text-lg">Enter news content below to verify its authenticity using Machine Learning.</p>
      </div>
      
      <div className="bg-card backdrop-blur-md p-8 rounded-2xl shadow-xl mb-10 border border-cardBorder hover:border-gray-700 transition-colors duration-300 relative overflow-hidden">
        {/* Subtle decorative glow */}
        <div className="absolute top-0 right-0 w-[300px] h-[300px] bg-accent/5 rounded-full blur-[80px] pointer-events-none transform translate-x-1/2 -translate-y-1/2"></div>
        
        <div className="flex justify-between items-center mb-6 relative z-10">
          <label className="text-sm font-semibold text-gray-300 uppercase tracking-widest">Select AI Model</label>
          <div className="relative">
            <select 
              value={model} 
              onChange={(e) => setModel(e.target.value)}
              className="appearance-none bg-[#0B152A] border border-cardBorder rounded-lg pl-4 pr-10 py-2.5 text-sm font-medium text-white focus:outline-none focus:border-accent focus:ring-1 focus:ring-accent transition-all cursor-pointer shadow-sm"
            >
              <option>Logistic Regression</option>
              <option>Multinomial Naive Bayes</option>
              <option>Random Forest</option>
            </select>
            <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-3 text-gray-400">
              <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
            </div>
          </div>
        </div>
        
        <div className="relative z-10">
          <textarea
            className="w-full bg-[#0B152A]/50 border border-cardBorder rounded-xl p-5 text-white focus:border-accent focus:ring-1 focus:ring-accent focus:outline-none min-h-[240px] mb-3 text-lg leading-relaxed placeholder-gray-600 transition-all resize-y shadow-inner"
            placeholder="Paste news headline or full article text here..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <div className="flex justify-between text-xs font-medium text-gray-500 mb-6 px-1">
            <span>{text.length} characters</span>
            <span>{wordCount} words</span>
          </div>
          
          {error && (
            <div className="bg-red-500/10 border border-red-500/20 text-red-400 text-sm font-medium mb-6 p-4 rounded-lg flex items-center gap-2 animate-fade-in">
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
              {error}
            </div>
          )}
          
          <button 
            onClick={handleCheck}
            disabled={loading}
            className="w-full bg-gradient-to-r from-accent to-orange-500 hover:from-orange-500 hover:to-orange-400 text-white font-extrabold py-4 px-6 rounded-xl shadow-glow hover:shadow-glow-green transform hover:-translate-y-1 transition-all duration-300 disabled:opacity-50 disabled:transform-none disabled:shadow-none disabled:cursor-not-allowed flex justify-center items-center gap-2 text-lg"
          >
            {loading ? (
              <>
                <svg className="animate-spin -ml-1 mr-2 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle><path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                Analyzing with AI...
              </>
            ) : 'Analyze Credibility'}
          </button>
        </div>
      </div>

      {result && (
        <div className="bg-card backdrop-blur-md p-8 rounded-2xl shadow-xl border border-cardBorder animate-slide-up relative overflow-hidden">
          {/* Result Background Glow */}
          <div className={`absolute top-0 right-0 w-[500px] h-[500px] rounded-full blur-[150px] pointer-events-none opacity-20 transform translate-x-1/2 -translate-y-1/2 ${result.prediction === 'REAL' ? 'bg-green-500' : 'bg-red-500'}`}></div>

          <div className="relative z-10">
            <h2 className="text-xl font-bold text-gray-200 mb-6 border-b border-cardBorder pb-4">Analysis Results</h2>
            
            <div className="flex flex-col md:flex-row items-start md:items-center gap-8 mb-8">
              <div className={`text-4xl md:text-5xl font-black px-8 py-4 rounded-2xl border ${
                result.prediction === 'REAL' 
                  ? 'bg-green-500/10 text-green-400 border-green-500/30 shadow-[0_0_30px_rgba(34,197,94,0.2)]' 
                  : 'bg-red-500/10 text-red-500 border-red-500/30 shell shadow-[0_0_30px_rgba(239,68,68,0.2)]'
              }`}>
                {result.prediction}
              </div>
              
              <div className="flex-1 w-full">
                <div className="flex justify-between items-end mb-2">
                  <span className="text-sm font-bold text-gray-400 uppercase tracking-wider">AI Confidence Score</span>
                  <span className="text-3xl font-extrabold text-white">{result.confidence.toFixed(1)}%</span>
                </div>
                <div className="w-full bg-[#0B152A] rounded-full h-3 shadow-inner overflow-hidden border border-cardBorder">
                  <div 
                    className={`h-full rounded-full transition-all duration-1000 ease-out relative ${result.prediction === 'REAL' ? 'bg-gradient-to-r from-green-600 to-green-400' : 'bg-gradient-to-r from-red-600 to-red-400'}`} 
                    style={{ width: `${result.confidence}%` }}
                  >
                    <div className="absolute top-0 right-0 bottom-0 w-10 bg-white/20 blur-[2px]"></div>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="bg-[#0B152A]/40 rounded-xl p-6 border border-cardBorder">
              <h3 className="text-sm font-bold text-gray-300 uppercase tracking-widest mb-4 flex items-center gap-2">
                <svg className="w-4 h-4 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                Linguistic Indicators
              </h3>
              <p className="text-xs text-gray-400 mb-4">The AI model identified these key words/n-grams as the strongest contributors to its decision:</p>
              <div className="flex flex-wrap gap-2.5">
                {result.explanation.map((word: string, i: number) => (
                  <span key={i} className="bg-card border border-cardBorder px-4 py-2 rounded-full text-sm font-semibold text-gray-200 shadow-sm hover:border-accent/50 hover:text-white transition-colors cursor-default">
                    {word}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
