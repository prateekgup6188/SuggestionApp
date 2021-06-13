from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json, requests
from dateutil import parser
from datetime import datetime
from google.oauth2 import service_account
from google.cloud import dialogflow
import os
import json
from chatApp.Intents import Scheduler,Reminder
# Create your views here.

@require_http_methods(['GET'])
def index_view(request):
    detect_intent_with_parameters()
    return render(request, 'chatApp/home.html')


## Function to call Dialogflow detectintent API endpoint
def detect_intent_with_parameters():
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversaion."""
    key_file_path = "C:/Users/jagra/nlp-jqut-609aa9c66364.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path
    GOOGLE_PROJECT_ID = "nlp-jqut"
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path('nlp-jqut','123456789')
    print('Session path: {}\n'.format(session))

    text = "Please book my appointment with Dr. Ram"

    text_input = dialogflow.TextInput(
        text=text, language_code="en-US")

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input,
    )

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))

    return response

@csrf_exempt
def webhook(request):
    # build a request object
    req = json.loads(request.body)
    data = req.get('queryResult').get('queryText')
    params = req.get('queryResult').get('parameters')
    intent =  req.get('queryResult').get('intent').get('displayName')
    mssg = ""

    if(intent=="Scheduler"):
        mssg = Scheduler.Schedule_Handler(params)
        
    elif(intent == "Reminder"):
        mssg = Reminder.Remind_Handler(params)
            
    print(mssg)
    
    fulfillmentText={'fulfillmentText':mssg}
    return JsonResponse(fulfillmentText, safe=False)
