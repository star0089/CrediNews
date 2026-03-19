import Link from 'next/link'

export default function Navbar() {
  return (
    <nav className="bg-[#050A14]/80 backdrop-blur-lg px-6 py-4 flex flex-wrap justify-between items-center sticky top-0 z-50 border-b border-cardBorder transition-all duration-300">
      <Link href="/" className="text-2xl font-extrabold flex items-center gap-2 text-white tracking-tight">
        Credi<span className="text-accent">News</span>
      </Link>
      <div className="flex flex-wrap gap-6 text-sm font-semibold items-center mt-4 md:mt-0 text-gray-300">
        <Link href="/" className="hover:text-white transition-colors duration-200">Home</Link>
        <Link href="/how-it-works" className="hover:text-white transition-colors duration-200">How It Works</Link>
        <Link href="/expected-results" className="hover:text-white transition-colors duration-200">Expected Results</Link>
        <Link href="/references" className="hover:text-white transition-colors duration-200">References</Link>
        <Link href="/check-news" className="bg-accent text-white px-5 py-2.5 rounded-full hover:bg-orange-500 shadow-glow hover:shadow-glow-green transform hover:-translate-y-0.5 transition-all duration-300 ml-2">
          Check News
        </Link>
      </div>
    </nav>
  )
}
