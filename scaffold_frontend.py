import os

frontend_files = {
    "frontend/package.json": """{
  "name": "credinews-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "axios": "^1.6.2",
    "clsx": "^2.1.0",
    "framer-motion": "^10.16.4",
    "lucide-react": "^0.292.0",
    "next": "14.0.3",
    "react": "^18",
    "react-dom": "^18",
    "tailwind-merge": "^2.0.0"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "autoprefixer": "^10.0.1",
    "postcss": "^8",
    "tailwindcss": "^3.3.0",
    "typescript": "^5"
  }
}
""",
    "frontend/tsconfig.json": """{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
""",
    "frontend/tailwind.config.ts": """import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: "#0A2540",
        accent: "#FF6B00",
        background: "#121212",
        card: "#1E1E1E"
      }
    },
  },
  plugins: [],
}
export default config
""",
    "frontend/postcss.config.js": """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
""",
    "frontend/next.config.mjs": """/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
};
export default nextConfig;
""",
    "frontend/app/globals.css": """@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  background-color: #121212;
  color: #ffffff;
}
""",
    "frontend/app/layout.tsx": """import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import Navbar from '@/components/Navbar'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'CrediNews: AI-Assisted Fake News Detection',
  description: 'Fight against fake news on the Internet',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Navbar />
        <main className="min-h-screen">
          {children}
        </main>
        <footer className="py-6 text-center text-sm text-gray-400 bg-primary mt-12">
          Authors: Mahesh Vyas & Jitendra Ghanchi | <a href="#" className="underline">GitHub</a>
        </footer>
      </body>
    </html>
  )
}
""",
    "frontend/components/Navbar.tsx": """import Link from 'next/link'

export default function Navbar() {
  return (
    <nav className="bg-primary px-6 py-4 flex justify-between items-center text-white sticky top-0 z-50 shadow-md">
      <Link href="/" className="text-xl font-bold flex items-center gap-2">
        CrediNews
      </Link>
      <div className="flex gap-4 text-sm font-medium">
        <Link href="/" className="hover:text-accent transition">Home</Link>
        <Link href="/how-it-works" className="hover:text-accent transition">How It Works</Link>
        <Link href="/check-news" className="bg-accent px-4 py-2 rounded-md hover:bg-orange-600 transition">Check News</Link>
      </div>
    </nav>
  )
}
""",
    "frontend/app/page.tsx": """import Hero from '@/components/Hero'

export default function Home() {
  return (
    <div>
      <Hero />
      <section className="max-w-4xl mx-auto py-12 px-6">
        <h2 className="text-3xl font-bold mb-6 text-accent">Abstract</h2>
        <p className="text-gray-300 leading-relaxed mb-8">
          The proliferation of fake news on social media and news platforms presents a significant threat to society...
          (Abstract from paper goes here)
        </p>

        <h2 className="text-3xl font-bold mb-6 text-accent">Introduction</h2>
        <p className="text-gray-300 leading-relaxed mb-4">
          In the digital age, information is consumed at an unprecedented rate. However, not all information is reliable...
          (Introduction from paper goes here)
        </p>
      </section>
    </div>
  )
}
""",
    "frontend/components/Hero.tsx": """export default function Hero() {
  return (
    <div className="bg-gradient-to-b from-primary to-background py-20 px-6 text-center border-b border-gray-800">
      <h1 className="text-4xl md:text-6xl font-bold text-white mb-6">
        Fight against fake news on the Internet
      </h1>
      <p className="text-lg md:text-xl text-gray-400 max-w-2xl mx-auto mb-8">
        CrediNews: AI-Assisted Fake News Detection System utilizing Machine Learning
        to provide instant credibility scores and analysis.
      </p>
    </div>
  )
}
""",
    "frontend/app/check-news/page.tsx": """'use client';
import { useState } from 'react';
import axios from 'axios';

export default function CheckNews() {
  const [text, setText] = useState('');
  const [model, setModel] = useState('Logistic Regression');
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const wordCount = text.trim() ? text.trim().split(/\\s+/).length : 0;

  const handleCheck = async () => {
    if (text.length < 20) {
      setError('Please enter at least 20 characters.');
      return;
    }
    setError('');
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/predict', {
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
""",
    "frontend/app/how-it-works/page.tsx": """export default function HowItWorks() {
  return (
    <div className="max-w-4xl mx-auto py-12 px-6">
      <h1 className="text-3xl font-bold mb-6 text-accent">How It Works</h1>
      
      <section className="mb-12">
        <h2 className="text-2xl font-bold mb-4">Methodology</h2>
        <p className="text-gray-300 mb-4">
          Our system utilizes Natural Language Processing (NLP) techniques and Machine Learning algorithms...
          (Methodology from paper)
        </p>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-bold mb-4">System Architecture</h2>
        <div className="bg-card p-6 rounded-lg font-mono text-sm text-gray-300 whitespace-pre overflow-x-auto border border-gray-800">
{`          [News Article/Headline]
                |
                v
        [Text Preprocessing]
      (Lowercase, Remove Punct, Stopwords)
                |
                v
        [TF-IDF Vectorization]
                |
                v
        [Machine Learning Model]
    (LogReg / Naive Bayes / Random Forest)
                |
                v
      [Prediction & Confidence Score]`}
        </div>
      </section>

      <section>
        <h2 className="text-2xl font-bold mb-4">Accuracy Metrics</h2>
        <ul className="list-disc pl-6 text-gray-300">
          <li>Logistic Regression: ~98%</li>
          <li>Multinomial Naive Bayes: ~93%</li>
          <li>Random Forest: ~99%</li>
        </ul>
      </section>
    </div>
  )
}
""",
    "frontend/Dockerfile": """FROM node:20-alpine
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build
CMD ["npm", "start"]
""",
    "docker-compose.yml": """version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend/models:/app/models
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000
    depends_on:
      - backend
""",
    "README.md": """# CrediNews: AI-Assisted Fake News Detection System

## HOW TO RUN

1. Start the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   python train_model.py  # Wait for training to finish
   uvicorn app.main:app --reload
   ```

2. Start the frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   Open `http://localhost:3000`

### OR Using Docker:
```bash
docker-compose up --build
```
"""
}

for path, content in frontend_files.items():
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Frontend scaffolded successfully.")
