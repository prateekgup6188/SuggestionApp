from django.urls import path
from chatApp import views

urlpatterns = [
    path('webhook', views.webhook, name='webhook'),
    path('updateCollection',views.update_collection, name="update_collection"),
    path('accuracy',views.accuracy_view, name="accuracy"),
    path('patientAccuracy',views.patient_accuracy, name="patient_accuracy")
]