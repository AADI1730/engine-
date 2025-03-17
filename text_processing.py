import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

def clean_text(text):
    words = word_tokenize(text.lower())  
    filtered_words = [word for word in words if word.isalnum() and word not in stopwords.words("english")]
    return " ".join(filtered_words)

# Example Usage
raw_text = "This is an example text for search engine development."
cleaned_text = clean_text(raw_text)
print(cleaned_text)
