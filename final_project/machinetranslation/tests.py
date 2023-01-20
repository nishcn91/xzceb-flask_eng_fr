import unittest

from translator import IBMTranslator

class TestTranslation(unittest.TestCase): 
    trans = IBMTranslator()
    def testE2f(self): 
        """
        tests for english to french translate
        """
        self.assertIsNone(self.trans.english_to_french(''))
        self.assertEqual(self.trans.english_to_french('Hello'),'Bonjour')
    
    def testF2e(self):
        """
        tests for french to english translate
        """
        self.assertIsNone(self.trans.french_to_english(''))
        self.assertEqual(self.trans.french_to_english('Bonjour'),'Hello')
  
unittest.main()