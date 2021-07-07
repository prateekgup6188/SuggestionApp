# Suggestion App


![Dialogflow](http://hirendave.tech/wp-content/uploads/2019/01/unnamed-1.png)

![Django + Python](https://www.ryadel.com/wp-content/uploads/2019/07/phyton-django-logo-735x300.jpg)

Django [Dialogflow](https://dialogflow.com) is a web client to chat with Dialogflow agent Suggestion-App.

Dialogflow is a natural language understanding platform used to design and integrate a conversational user interface into mobile apps, web applications, devices, bots, interactive voice response systems and related uses.

## Setup Instructions

### Download and run the app
The following sections guides you through configuring and running the sample.

Clone the Django app

Clone the repository to your local machine:
```js 
git clone https://github.com/prateekgup6188/SuggestionApp.git
```
cd into the directory that contains the code.
Alternatively, you can download the sample as a zip and extract it.

### Service Account Setup
1. In Dialogflow's console, go to settings ⚙ and under the general tab, you'll see the project ID section with a Google Cloud link to open the Google Cloud console. Open Google Cloud.
2. In the Cloud console, go to the menu icon **☰ > APIs & Services > Credentials**
3. Under the menu icon **☰ > APIs & Services > Credentials > Create Credentials > Service Account Key**.
4. Under Create service account key, select New Service Account from the dropdown and enter. If you already have a service account key, select that. 
5. AppointmentCalendar for the name and click Create. In the popup, select Create Without Role.
6. JSON file will be downloaded to your computer that you will need in the setup sections below.

### Set up Dialogflow DetectIntent endpoint to be called from the App
Create a .env file in your root project directory and add "KEY_PATH", "GOOGLE_PROJECT_ID" and "SESSION_ID"(use "123456789" as default) from the JSON file.
Create new agent and start making intents and their default responses in dialogflow to train your model.
```js
https://dialogflow.cloud.google.com/
```

### Build and run the app locally
To run the Django app on your local computer, you'll need to set up a Python development environment, including Python, pip, and virtualenv. For instructions, refer to Setting Up a Python Development Environment for Google Cloud Platform.

Create an isolated Python environment, and install dependencies:
```js
virtualenv env -p python
source env/bin/activate
pip install -r requirements.txt
pip install Django
```
Run the Django migrations to set up your models:
```js
python manage.py makemigrations
python manage.py migrate
```
Start a local web server:
```js
python manage.py runserver
```

### Send data using Postman to test the App

Install Postman app on your device
```js 
https://www.postman.com/
```
To get suggestions for given text, use the following API to send data via Postman:-
```js
http://localhost:8000
```
![Get_Suggestion Request](https://github.com/prateekgup6188/SuggestionApp/blob/master/PatientApp/screenshots/get-suggestions.png)

To check accuracy of complete model, use the following API to send data via Postman:-
```js
http://localhost:8000/chatApp/accuracy
```
![Get_Accuracy Request](https://github.com/prateekgup6188/SuggestionApp/blob/master/PatientApp/screenshots/get-accuracy.png)


To train existing model on a bunch of notes in a CSV file, use the following API to send data via Postman:-
```js
http://localhost:8000/chatApp/updateCollection
```
![Sample CSV file](https://github.com/prateekgup6188/SuggestionApp/blob/master/PatientApp/screenshots/CSV%20file.png)
![Update Collection Request](https://github.com/prateekgup6188/SuggestionApp/blob/master/PatientApp/screenshots/update-collection.png)


To check accuracy of model for  particular patient, use the following API to send data via Postman:-
```js
http://localhost:8000/chatApp/patientAccuracy?id={x}
```
![Patient Accurcy Request](https://github.com/prateekgup6188/SuggestionApp/blob/master/PatientApp/screenshots/patient-accuracy.png)

I have also integrated the project with MongoDB database for storing suggestion response for a given text using Suggest model in Django.

## Tech Stack
1. Dialogflow
2. Django
3. Python
4. Postman

