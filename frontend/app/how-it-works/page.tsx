export default function HowItWorks() {
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
