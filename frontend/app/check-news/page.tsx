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
    <div className="max-w-4xl mx-auto py-12 px-6">
      <h1 className="text-3xl font-bold mb-6 text-accent">Check News Credibility</h1>
      
      <div className="bg-card p-6 rounded-lg shadow-lg mb-8 border border-gray-800">
        <div className="flex justify-between items-center mb-4">
          <label className="text-sm font-medium text-gray-300">Select Model</label>
          <select 
            value={model} 
            onChange={(e) => setModel(e.target.value)}
            className="bg-background border border-gray-700 rounded px-3 py-1 text-sm text-white focus:outline-none"
          >
            <option>Logistic Regression</option>
            <option>Multinomial Naive Bayes</option>
            <option>Random Forest</option>
          </select>
        </div>
        
        <textarea
          className="w-full bg-background border border-gray-700 rounded-lg p-4 text-white focus:border-accent focus:outline-none min-h-[200px] mb-2"
          placeholder="Paste news headline or article here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <div className="flex justify-between text-xs text-gray-500 mb-4">
          <span>{text.length} characters</span>
          <span>{wordCount} words</span>
        </div>
        
        {error && <div className="text-red-500 text-sm mb-4">{error}</div>}
        
        <button 
          onClick={handleCheck}
          disabled={loading}
          className="w-full bg-accent hover:bg-orange-600 text-white font-bold py-3 px-4 rounded transition-colors disabled:opacity-50"
        >
          {loading ? 'Analyzing with AI...' : 'Analyze Credibility'}
        </button>
      </div>

      {result && (
        <div className="bg-card p-6 rounded-lg shadow-lg border border-gray-800 animate-in fade-in slide-in-from-bottom-4">
          <div className="flex items-center gap-4 mb-6">
            <div className={`text-2xl font-bold px-4 py-2 rounded-full ${result.prediction === 'REAL' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
              {result.prediction}
            </div>
            <div>
              <div className="text-sm text-gray-400">Credibility Score</div>
              <div className="text-2xl font-bold">{result.confidence.toFixed(1)}%</div>
            </div>
          </div>
          
          <div className="w-full bg-gray-700 rounded-full h-2.5 mb-6">
            <div 
              className={`h-2.5 rounded-full ${result.prediction === 'REAL' ? 'bg-green-500' : 'bg-red-500'}`} 
              style={{ width: `${result.confidence}%` }}
            ></div>
          </div>
          
          <div>
            <h3 className="text-sm font-medium text-gray-300 mb-2">Explanation (Top Features):</h3>
            <div className="flex flex-wrap gap-2">
              {result.explanation.map((word: string, i: number) => (
                <span key={i} className="bg-primary px-3 py-1 rounded-full text-xs text-blue-300">
                  {word}
                </span>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
