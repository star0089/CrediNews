import os

frontend_updates = {
    "frontend/app/page.tsx": """import Hero from '@/components/Hero'

export default function Home() {
  return (
    <div>
      <Hero />
      <section className="max-w-4xl mx-auto py-12 px-6">
        <h2 className="text-3xl font-bold mb-6 text-accent">Abstract</h2>
        <p className="text-gray-300 leading-relaxed mb-8">
          The fast development of digital media and social networking sites have contributed at a bigger rate to the dissemination of fake news and misinformation. The spread of false information is more rapid than the factual news and may adversely affect the populace opinion, especially in young individuals who use online sources and platforms as the main sources of information. The growing amount of digital content renders the process of manually fact-checking ineffective and time consuming. The research suggests the CrediNews, which is an AI based fake news detection system, a system that employs both the approach of machine learning and Natural Language Processing (NLP) to determine fake or misleading news stories. The system uses textual trends, language, and context in determining that news is real or fake and gives a credibility rating. Through the combination of automated checks and an open web interface, CrediNews will of course encourage responsible consumption of information and curb misinformation distribution. The proposed system shows the way in which artificial intelligence could be used to help users verify digital content most efficiently and enhance media literacy in contemporary digital spaces.
        </p>

        <h2 className="text-3xl font-bold mb-6 text-accent">Introduction</h2>
        <p className="text-gray-300 leading-relaxed mb-4">
          The information creation, sharing, and consumption have been changed by the digital revolution. Passing through social media and websites that news is delivered and apps of messaging services, now serve as the sources of information to millions of people. On the one hand, these platforms allow a high rate of exchanging information; on the other hand, they make it possible to spread false news and misinformation in general.
        </p>
        <p className="text-gray-300 leading-relaxed mb-4">
          Fake news is a type of misrepresented information or deliberately false news that is passed as an honest news item. This kind of content will usually be constructed to influence views, present confusion or produce emotional responses in readers. Fake news can easily be transmitted among millions of users in minutes with the emergence of social media, which makes it impossible to manage. Young people are the special group which is liable to misinformation as they often use digital means of news delivery and social communication. In the absence of efficient check systems, users can easily post deceptive information unknowingly and this is one of the factors that propagate misinformation quickly.
        </p>
        <p className="text-gray-300 leading-relaxed mb-4">
          The old methods of fact checking are time consuming and involve human checks, research and great number of research, which cannot be easier with the volume of information that is produced online daily. Hence, there is an increasing necessity of automated systems that can identify fake news at an efficient and rapid step.
        </p>
        <p className="text-gray-300 leading-relaxed mb-4">
          In this work, the author presents a CrediNews, the artificial intelligence-powered fake news detector, which aims to analyze textual data and define whether it is plausible or not, with the use of machine learning methods. The system can enable its users to write in news content and have an immediate forecast on whether the news information is real or fake. The main idea of this project is to come up with a dependable and easily accessible system which assists the users to check digital materials as well as promote responsible sharing of information.
        </p>

        <h2 className="text-3xl font-bold mb-6 text-accent mt-12">Problem Statement</h2>
        <p className="text-gray-300 leading-relaxed mb-4">
          Fake news diffusion has been regarded as one of the largest problems of digital communication in recent years. Facts that are false or contradictory may alter views on political matters, break social ground, evoke panic and weaken the objectivity of journalism as an institution.
        </p>
        <p className="text-gray-300 leading-relaxed mb-4">
          The absence of available verification tools in the hands of the common users is one of the most significant problems that propagated the spread of fake news. Headlines or posts in social media have been trusted by many without any verification of their authenticity. Such attitude gives the possibility to misinform many people at once through the Internet.
        </p>
        <p className="text-gray-300 leading-relaxed mb-4">
          There are manual fact-checking organizations that cannot cope with the vast amount of information produced on the internet on a daily basis. Moreover, the users tend to share the news stories without even checking the origin and evaluating the validity of the information.
        </p>
        <p className="text-gray-300 leading-relaxed mb-4">
          Due to those difficulties, an automated system, which could analyze news materials, and identify the possible information misconduct, is needed. Through the use of Artificial Intelligence, Machine Learning and Natural Language Processing, it can find linguistic patterns and characteristics that are often related with fake news.
        </p>
      </section>
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
        <p className="text-gray-300 mb-4 leading-relaxed">
          The given system is based on the combination of Natural Language Processing (NLP) and Machine Learning algorithms to interpret the textual information and categorize news articles as real and fake.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          CrediNews has its development process that consists of several steps.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          To begin with, a collection of real and fake news articles is done based on publicly available sources, e.g. online news datasets. These datasets are lawed instances that enable the machine learning model to get to know patterns of various news.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          The text data then goes through preprocessing which involves cleaning of the text, i.e. removing punctuates, turning the text to lowercase and deleting the common stop words that do not add up to any meaningful analysis. The step will guarantee that the model concentrates on pertinent linguistic data.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          On preprocessing the text data is transformed into numerical features with the help of the TF-IDF (Term Frequency - Inverse Document Frequency) method. Such an approach is a representation of text data in an arithmetic form that can be modeled efficiently by machine learning.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          After data is converted into feature vectors then a machine learning model can be trained with a Logistic Regression, Naive Bayes or Random Forest as examples. Such algorithms identify trends in the collection of data and learn to differentiate between authentic and fake news.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          The trained model is then incorporated into a web based application which enables a user to enter in news text. The text is processed by the system and passed through the trained model and a prediction of whether the news is more likely to be real or fake generated and returned.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          Besides, the system includes a credibility score that indicates the level of confidence of the prediction. This score allows the users to evaluate the trustfulness of the analyzed material much better.
        </p>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-bold mb-4">System Architecture</h2>
        <p className="text-gray-300 mb-4 leading-relaxed">
          CrediNews system comprises a number of interrelated components that have a collaborative process in detecting fake news. It starts with the user interface whereby the user enters the headlines in a news or an article. This is forwarded to the backend server where it is processed.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          The backend carries out preprocessing of a text and translates the input text into a numerical feature through the NLP methods. These features are then inputted into the trained machine learning model hence coming with a prediction derived by the patterns that the machine had been trained upon.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          Prediction results with a credibility score are sent back to the user interface and they are presented in a simple and understandable format.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          The architecture may be concluded as the following:
        </p>
        <div className="bg-card p-6 rounded-lg font-mono text-sm text-gray-300 whitespace-pre overflow-x-auto border border-gray-800 mt-6">
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
    </div>
  )
}
""",
    "frontend/app/expected-results/page.tsx": """export default function ExpectedResults() {
  return (
    <div className="max-w-4xl mx-auto py-12 px-6">
      <h1 className="text-3xl font-bold mb-6 text-accent">Expected Results & Conclusion</h1>
      
      <section className="mb-12">
        <h2 className="text-2xl font-bold mb-4">Expected Results</h2>
        <p className="text-gray-300 mb-4 leading-relaxed">
          CrediNews system will make it to a high accuracy: the system will recognize real upcoming news and fake news based on the linguistic feature and text-based patterns. Machine learning algorithms can be trained on massive data to attain classification accuracy of over 90%.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          The system will ensure that the users do not spread misleading information by quickly and automatically checking the content of the news first. This will help decrease the misinformation and promote the responsible consumption of information.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          The system also seeks to sensitize the youthful users about fake news by encouraging critical thinking and digital literacy.
        </p>
      </section>

      <section>
        <h2 className="text-2xl font-bold mb-4">Conclusion</h2>
        <p className="text-gray-300 mb-4 leading-relaxed">
          The phenomenon of the spreading fake news poses a severe threat to the contemporary digital society. Propaganda has the ability to shape the perception of the people, make them socially divided, and lose trust in the credible sources of information.
        </p>
        <p className="text-gray-300 mb-4 leading-relaxed">
          The proposed study is based on the fake news detector named CrediNews that is an AI based platform that detects misleading information by using algorithms based on the principle of Natural Language Processing and Machine Learning. The system assists users to check the news content of a certain news item by analysing the text features and giving credibility scores in a quick and effective manner.
        </p>
      </section>
    </div>
  )
}
""",
    "frontend/app/references/page.tsx": """export default function References() {
  return (
    <div className="max-w-4xl mx-auto py-12 px-6">
      <h1 className="text-3xl font-bold mb-6 text-accent">References</h1>
      
      <div className="bg-card p-6 rounded-lg shadow-lg border border-gray-800">
        <ul className="list-decimal pl-6 text-gray-300 space-y-4">
          <li>
            H. Allcott and M. Gentzkow, "Social Media and Fake News in the 2016 Election," <em>Journal of Economic Perspectives</em>, vol. 31, no. 2, pp. 211–236, 2017.
          </li>
          <li>
            S. Vosoughi, D. Roy, and S. Aral, "The spread of true and false news online," <em>Science</em>, vol. 359, no. 6380, pp. 1146-1151, 2018.
          </li>
          <li>
            K. Shu, A. Sliva, S. Wang, J. Tang, and H. Liu, "Fake News Detection on Social Media: A Data Mining Perspective," <em>ACM SIGKDD Explorations Newsletter</em>, vol. 19, no. 1, 2017.
          </li>
          <li>
            J. Zhou and F. Zafarani, "Fake News: A Survey of Research, Detection Methods, and Opportunities," <em>ACM Computing Surveys</em>, vol. 53, no. 5, 2020.
          </li>
          <li>
            G. Salton and C. Buckley, "Term weighting approaches in automatic text retrieval," <em>Information Processing & Management</em>, vol. 24, no. 5, pp. 513–523, 1988.
          </li>
          <li>
            C. M. Bishop, <em>Pattern Recognition and Machine Learning</em>. New York: Springer, 2006.
          </li>
          <li>
            N. Ruchansky, S. Seo, and Y. Liu, "CSI: A Hybrid Deep Model for Fake News Detection," <em>Proc. ACM Int. Conf. Information and Knowledge Management</em>, 2017.
          </li>
        </ul>
      </div>
    </div>
  )
}
""",
    "frontend/components/Navbar.tsx": """import Link from 'next/link'

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
          Authors: Mahesh Vyas (maheshvyas.data@gmail.com) & Jitendra Ghanchi (jeetuparihariya@gmail.com) | <a href="#" className="underline">GitHub</a>
        </footer>
      </body>
    </html>
  )
}
"""
}

for path, content in frontend_updates.items():
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Frontend pages updated with PDF text successfully.")
