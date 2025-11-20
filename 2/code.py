import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from collections import defaultdict
import nltk

def tokenization():
    # start code here
    # end code here
    pass

def bag_of_words():
    # start code here
    # end code here
    pass

def tf_idf():
    # start code here
    # end code here
    pass

def glove_embeddings():
    # start code here
    # end code here
    pass

def sentiment_analysis_nb():
    # start code here
    # end code here
    pass

def pos_tagging_viterbi():
    # start code here
    # end code here
    pass

def ngram_bigram():
    # start code here
    # end code here
    pass

if __name__ == "__main__":
    print("Tokenization")
    tokenization()
    print("-" * 10)
    print("Bag of Words")
    bag_of_words()
    print("-" * 10)
    print("TF-IDF")
    tf_idf()
    print("-" * 10)
    print("GloVe (Simulated)")
    glove_embeddings()
    print("-" * 10)
    print("Sentiment Analysis (Naive Bayes)")
    sentiment_analysis_nb()
    print("-" * 10)
    print("POS Tagging (Viterbi)")
    pos_tagging_viterbi()
    print("-" * 10)
    print("N-Gram (Bigram)")
    ngram_bigram()
