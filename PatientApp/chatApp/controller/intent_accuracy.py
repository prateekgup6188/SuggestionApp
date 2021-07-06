import os
from google.cloud import dialogflow
from dotenv import load_dotenv
from chatApp.models import Accuracy_DB
load_dotenv()

def get_notes(patient_id):
    if(patient_id == -1):
        return Accuracy_DB.objects.filter()
    return Accuracy_DB.objects.filter(patient_id=patient_id)

def get_accuracy(patient_id = -1):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv('KEY_PATH')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(os.getenv('GOOGLE_PROJECT_ID'),os.getenv('SESSION_ID'))
    cnt = 0
    data = get_notes(patient_id)
    for sentence in data.iterator(): 
        text_input = dialogflow.TextInput(text=sentence.text, language_code="en-US")
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input,)
        if(response.query_result.intent.display_name == sentence.intent):
            cnt = cnt + 1
        else:
            print("This one is wrong --> ",sentence.text," Original Intent --> ",sentence.intent,", Found Intent --> ",response.query_result.intent.display_name)
    avg = (cnt * 100) / len(data)
    return avg   