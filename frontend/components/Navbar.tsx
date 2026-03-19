import Link from 'next/link'

export default function Navbar() {
  return (
    <nav className="bg-primary px-6 py-4 flex flex-wrap justify-between items-center text-white sticky top-0 z-50 shadow-md">
      <Link href="/" className="text-xl font-bold flex items-center gap-2">
        CrediNews
      </Link>
      <div className="flex flex-wrap gap-4 text-sm font-medium items-center mt-4 md:mt-0">
        <Link href="/" className="hover:text-accent transition">Home</Link>
        <Link href="/how-it-works" className="hover:text-accent transition">How It Works</Link>
        <Link href="/expected-results" className="hover:text-accent transition">Expected Results</Link>
        <Link href="/references" className="hover:text-accent transition">References</Link>
        <Link href="/check-news" className="bg-accent px-4 py-2 rounded-md hover:bg-orange-600 transition ml-2">Check News</Link>
      </div>
    </nav>
  )
}
