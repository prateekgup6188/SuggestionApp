import os
from google.cloud import dialogflow
from chatApp.handler import filter_data_handler,detect_tense
from chatApp.models import Suggest
from dotenv import load_dotenv
load_dotenv()


def get_suggestions(patient_id,note_id,text):
     
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv('KEY_PATH')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(os.getenv('GOOGLE_PROJECT_ID'),os.getenv('SESSION_ID'))
    sentences = filter_data_handler.clean_data(text)
    suggestions = []
    for sentence in sentences: 
        text_input = dialogflow.TextInput(text=sentence, language_code="en-US")
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input,)

        if(response and response.query_result.fulfillment_text):
            suggestions.append((response.query_result.fulfillment_text,response.query_result.query_text,response.query_result.intent.display_name))
            
            # To save text and corresponding response in Database
            suggestion = Suggest(
                text = response.query_result.query_text,
                response = response.query_result.fulfillment_text,
                patient_id = patient_id,
                note_id = note_id
            )
            suggestion.save()
    print(suggestions)
