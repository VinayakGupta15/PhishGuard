import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
import joblib

# Download NLTK resources
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load dataset
df = pd.read_csv('dataset.csv')
df['label'] = df['label'].map({'phishing': 1, 'not phishing': 0})

# Preprocess text
def preprocess_text(text):
    text = text.lower()
    tokens = [word for word in text.split() if word not in stop_words]
    return " ".join(tokens)

df['message'] = df['message'].apply(preprocess_text)

# Split data
X = df['message']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=3000)
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Save vectorizer and data
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
joblib.dump((X_train, X_test, y_train, y_test), 'processed_data.pkl')
print("Data preparation complete.")
