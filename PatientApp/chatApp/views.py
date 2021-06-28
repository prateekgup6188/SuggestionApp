from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json, requests
from chatApp.Intents import Scheduler,Reminder
from chatApp.controller import suggestion,intent_accuracy
# Create your views here.

@require_http_methods(['GET'])
def index_view(request):
    req = json.loads(request.body)
    data = req.get('text')
    suggestion.get_suggestions(data)
    return render(request,'chatApp/home.html')

@require_http_methods(['GET'])
def accuracy_view(request):
    req = json.loads(request.body)
    data = req.get('text')
    avg = intent_accuracy.get_accuracy(data)
    print(avg)
    return render(request,'chatApp/home.html')

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
            
    # print(mssg)
    
    fulfillmentText={'fulfillmentText':mssg}
    return JsonResponse(fulfillmentText, safe=False)
