import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

# Create NLP objects
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    """
    Clean and preprocess text for the recommendation system.
    """

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Split text into words
    words = text.split()

    # Remove stopwords and apply lemmatization
    cleaned_words = []

    for word in words:
        if word not in stop_words:
            word = lemmatizer.lemmatize(word)
            cleaned_words.append(word)

    # Join words back into a sentence
    return " ".join(cleaned_words)