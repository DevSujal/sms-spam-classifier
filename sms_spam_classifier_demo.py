
import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

tfidf = TfidfVectorizer()

nltk.download('punkt')
nltk.download('punkt_tab')

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

import string
def transform_text(text):
  text = text.lower();
  text = nltk.word_tokenize(text)

  y = []
  for i in text:
    if i.isalnum():
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    if i not in stop_words and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("SMS Spam Classifier")
message = st.text_area("Enter a message")

# 1. Preprocess the message
# 2. Vectorize the message
# 3. Predict the message
# 4. Display the prediction

if st.button("Predict"):
    message = transform_text(message)
    tokenized_message = tfidf.transform([message])
    prediction = model.predict(tokenized_message)
    if prediction[0] == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")


