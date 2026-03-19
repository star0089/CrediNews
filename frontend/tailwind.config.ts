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
