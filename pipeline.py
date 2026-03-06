import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
from nltk.sentiment import SentimentIntensityAnalyzer
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except nltk.downloader.DownloadError:
    nltk.download('vader_lexicon')
texts = ["I love this product!", "This is terrible.", "What a fantastic day!", "I hate this experience."]
labels = ["positive", "negative", "positive", "negative"]
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=1)
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)
classifier = MultinomialNB()
classifier.fit(X_train_counts, y_train)
predicted = classifier.predict(X_test_counts)
print("Classification Report:")
print(metrics.classification_report(y_test, predicted)) 
sia = SentimentIntensityAnalyzer()
new_text = "I absolutely love this!"
scores = sia.polarity_scores(new_text)
sentiment = "positive" if scores['compound'] >= 0.05 else ("negative" if scores['compound'] <= -0.05 else "neutral")
print(f"\nText: '{new_text}' | Sentiment: {sentiment} | Scores: {scores}")

