import logging
import math
import operator
from time import sleep
from creepy import Crawler

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class tdidf:
    def __init__(self):
        self.corpus = None
        self._load_text()
        self.list_of_words_in_visible_page_text = None

    def _load_text(self):
        text = open('corpus.txt', 'r')
        self.corpus = map(str.strip, text.readlines())
        text.close()

    def top_words(self, number_of_terms, list_of_words_in_visible_page_text):
        results = {}
        self.list_of_words_in_visible_page_text = list_of_words_in_visible_page_text
        for word in list_of_words_in_visible_page_text:
            word = word.lower().strip()
            if word not in results:
                results[word] = self.tfidf(word, list_of_words_in_visible_page_text, [list_of_words_in_visible_page_text, self.corpus])
        sorted_results = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
        return_results = []
        count = 0
        for i in sorted_results:
            if count > number_of_terms:
                return return_results 
            return_results.append(i)
            count += 1
        return return_results

    '''TFIDF Logic'''
    def tf(self, word, text):
        return float(text.count(word)) / len(self.list_of_words_in_visible_page_text)

    def n_containing(self, word, bloblist):
        return sum(1 for blob in bloblist if unicode(word) == unicode(blob))

    def idf(self, word, listoftexts):
        try:
            return math.log(len(listoftexts) / float(1 + self.n_containing(word, listoftexts)))
        except Exception as e:
            print e
            return 0

    def tfidf(self, word, text, text_list):
        return self.tf(word, text) * self.idf(word, text_list)