import nltk
import os
from nltk.tokenize import sent_tokenize, word_tokenize
import json, requests
from datetime import datetime
from google.oauth2 import service_account
from google.cloud import dialogflow
from chatApp.handler import filter_data_handler,detect_tense
from chatApp.models import Suggest
from dotenv import load_dotenv
load_dotenv()


def get_suggestions(text):
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv('KEY_PATH')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(os.getenv('GOOGLE_PROJECT_ID'),os.getenv('SESSION_ID'))

    filtered_chat = filter_data_handler.clean_data(text)
    sentences = sent_tokenize(filtered_chat)
    suggestions = []
    for sentence in sentences: 
        # tense = detect_tense.determine_tense(sentence)
        # if(tense != "past"):
        text_input = dialogflow.TextInput(text=sentence, language_code="en-US")
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input,)

        if(response and response.query_result.intent and response.query_result.intent.display_name != 'Default Fallback Intent' and response.query_result.intent.display_name != 'Default Welcome Intent'):
            suggestions.append((response.query_result.fulfillment_text,response.query_result.intent.display_name))
            # suggestion = Suggest(
            #     text = response.query_result.query_text,
            #     response = response.query_result.fulfillment_text,
            #     intent = response.query_result.intent.display_name
            # )
            # suggestion.save()
    print(suggestions)
