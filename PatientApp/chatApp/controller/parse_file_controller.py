import csv
from chatApp.models import Accuracy_DB
from chatApp.handler import filter_data_handler

def parse_file(file):
    nfile = file.read().decode('utf-8-sig').splitlines()
    reader = csv.DictReader(nfile)
    for data in reader:
        text = filter_data_handler.clean_data(data.get('Text'))   
        obj = Accuracy_DB(patient_id = data.get('Patient_id'), text = str(text[0]), intent = data.get('Intent'))
        obj.save()
