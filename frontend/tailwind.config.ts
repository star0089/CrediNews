import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: "#0B152A",
        accent: "#F97316",
        background: "#050A14",
        card: "rgba(30, 41, 59, 0.4)", // Translucent slate for glassmorphism
        cardBorder: "rgba(255, 255, 255, 0.05)",
      },
      boxShadow: {
        'glow': '0 0 20px rgba(249, 115, 22, 0.3)',
        'glow-green': '0 0 25px rgba(34, 197, 94, 0.4)',
        'glow-red': '0 0 25px rgba(239, 68, 68, 0.4)',
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out forwards',
        'slide-up': 'slideUp 0.6s ease-out forwards',
        'shimmer': 'shimmer 2s linear infinite',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        shimmer: {
          from: { backgroundPosition: '200% 0' },
          to: { backgroundPosition: '-200% 0' }
        }
      }
    },
  },
  plugins: [],
}
export default config
