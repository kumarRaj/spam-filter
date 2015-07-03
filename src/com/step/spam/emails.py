from collections import defaultdict
from decimal import *


class Emails(object):
    def __init__(self, file):
        self.all_words = defaultdict(list)
        for aLine in file.xreadlines():
            words = aLine.split()
            label = words[0]
            words = words[1:]
            self.all_words[label] += words

    def allWords(self):
        return self.all_words["1"] + self.all_words["0"]


    def allSpamWords(self):
        return self.all_words["1"]


    def wordFrequencyMap(self):
        all_words = self.allWords()
        frequencyMap = defaultdict(int)
        for aWord in all_words:
            frequencyMap[aWord] += 1
        return frequencyMap

    def spamWordFrequencyMap(self):
        all_spam_words = self.allSpamWords()
        frequencyMap = defaultdict(int)
        for aWord in all_spam_words:
            frequencyMap[aWord] += 1
        return frequencyMap

    def probabilityOf(self, word):
        return Decimal(self.wordFrequencyMap()[word]) / Decimal(len(set(self.allWords())))

    def probabilityOfWordGivenSpam(self, word):
        return Decimal(self.spamWordFrequencyMap()[word]) / Decimal(len(set(self.allSpamWords())))

    def probabilityOfEmailBeingSpam(self, words):
        partOfNumerator = Decimal(1)
        denominator = Decimal(0)
        for word in words:
            partOfNumerator *= Decimal(self.probabilityOfWordGivenSpam(word))
            denominator += Decimal(self.probabilityOf(word))
        return (partOfNumerator * Decimal(0.5)) / denominator