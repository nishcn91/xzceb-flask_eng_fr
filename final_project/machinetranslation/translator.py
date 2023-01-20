"""
Translation Module - IBMTranslator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.api_exception import ApiException
from dotenv import load_dotenv

load_dotenv()

class IBMTranslator():
    """
    class for the helper methods to access IBM translator
    """
    apikey = os.environ['apikey']
    url = os.environ['url']
    version = os.environ['version']
    def __init__(self):
        self.authenticator = IAMAuthenticator(self.apikey)
        self.language_translator = LanguageTranslatorV3(
            version=self.version,
            authenticator=self.authenticator
        )
        self.language_translator.set_service_url(self.url)
        self.english_text = ''
        self.french_text = ''
        self.result = ''

    def english_to_french(self, english_text):
        """
        fetch a statement in english and translate to french
        in case of any APIException return null
        """
        self.english_text = english_text
        try:
            self.result = self.language_translator.translate(
            text=self.english_text,
            model_id='en-fr').get_result()['translations']
            return self.result[0]['translation']
        except ApiException:
            return None

    def french_to_english(self, french_text):
        """
        fetch a statement in french and translate to english
        in case of any APIException return null
        """
        self.french_text = french_text
        try:
            self.result = self.language_translator.translate(
            text=self.french_text,
            model_id='fr-en').get_result()['translations']
            return self.result[0]['translation']
        except ApiException:
            return None

ENGLISH_STRING = 'Hi, How do I get to the railway station?'
translator_obj = IBMTranslator()
frenchText = translator_obj.english_to_french(ENGLISH_STRING)
FRENCH_STRING = 'Salut, comment puis-je me rendre à la gare?'
englishText = translator_obj.french_to_english(FRENCH_STRING)
