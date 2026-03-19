import type { Metadata } from 'next'
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
          Authors: Mahesh Vyas (maheshvyas.data@gmail.com) & Jitendra Ghanchi (jeetuparihariya@gmail.com) | <a href="#" className="underline">GitHub</a>
        </footer>
      </body>
    </html>
  )
}
