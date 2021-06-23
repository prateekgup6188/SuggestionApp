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


def get_accuracy(data):
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv('KEY_PATH')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(os.getenv('GOOGLE_PROJECT_ID'),os.getenv('SESSION_ID'))
    cnt = 0
    for sentence in data: 
        # tense = detect_tense.determine_tense(sentence)
        # if(tense != "past"):
        text_input = dialogflow.TextInput(text=sentence[0], language_code="en-US")
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input,)

        if(response and response.query_result.intent and response.query_result.intent.display_name == sentence[1]):
            cnt = cnt + 1
        else:
            print("This one is wrong --> ",sentence[0]," Original Intent --> ",sentence[1]," Found Intent --> ",response.query_result.intent.display_name)
    avg = (cnt * 100) / len(data)
    return avg   