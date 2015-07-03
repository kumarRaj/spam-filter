import unittest

from com.step.spam import *
from decimal import *


class TestEmails(unittest.TestCase):

    def setUp(self):
        file = open("../../../resources/documents")
        self.emails = Emails(file)

    def test_shouldGetAllWords(self):
        allWords = self.emails.allWords()
        self.assertEqual(len(allWords), 59)

    def test_shouldGetAllSpamWords(self):
        allWords = self.emails.allSpamWords()
        self.assertEqual(len(allWords), 32)

    def test_shouldGetWordCountOfEveryWord(self):
        frequencyMap = self.emails.wordFrequencyMap()
        self.assertEqual(frequencyMap["offer"], 4)
        self.assertEqual(frequencyMap["congratulations"], 1)

    def test_shouldGetWordCountOfEverySpamWord(self):
        spamFrequencyMap = self.emails.spamWordFrequencyMap()
        self.assertEqual(spamFrequencyMap["offer"], 3)
        self.assertEqual(spamFrequencyMap["congratulations"], 1)

    def test_shouldCalculateProbabilityOfWord(self):
        probability = self.emails.probabilityOf("offer")
        self.assertEquals(Decimal(4)/Decimal(59), probability)

    def test_shouldCalculateProbabilityOfWordGivenSpam(self):
        probability = self.emails.probabilityOfWordGivenSpam("offer")
        self.assertEquals(Decimal(3)/Decimal(32), probability)

    def test_shouldCalculateProbabilityGivenEmailBeingSpam(self):
        probability = self.emails.probabilityOfEmailBeingSpam(["offer", "win", "congratulations"])
        self.assertEqual(0,probability)

