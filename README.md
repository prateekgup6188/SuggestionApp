# Django Dialogflow GoogleVisionAPI Suggestion App
Django [Dialogflow](https://dialogflow.com) is a web client to chat with Dialogflow agent Suggestion-App.

## Setup Instructions

### Download and run the app
The following sections guide you through configuring and running the sample.

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
1. In views.py in chat folder, Change the GOOGLE_PROJECT_ID = **"<YOUR_PROJECT_ID>"** to your project ID

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
python manage.py makemigrations polls
python manage.py migrate
```
Start a local web server:
```js
python manage.py runserver
```
In your web browser, enter this address:

http://localhost:8000/
