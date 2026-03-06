import math
import numpy as np
from collections import Counter
import re
import nltk
from nltk import ngrams
nltk.download('punkt')
def calculate perplexity (text, n = 2 ):
"""Calculates the perplexity of text using a simple n-gram model."""
11 text = re.sub(r'[^\w\s]', text.lower()) # Simple preprocessing
tokens = nltk.word tokenize (text)
if not tokens: return 0.0
# Use bigrams for demonstration
n grams list (ngrams (tokens, n))
freq dist = nltk. FreqDist(n grams)
# Calculate entropy
N= len(n grams)
entropy = sum(freq dist [ng] math.log2(freq dist[ng]/N) for ng in freq dist)