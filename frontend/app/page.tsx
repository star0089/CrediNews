import Hero from '@/components/Hero'

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
