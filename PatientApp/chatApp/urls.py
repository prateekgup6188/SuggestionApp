from django.urls import path
from chatApp import views

urlpatterns = [
    path('webhook/', views.webhook, name='webhook'),
]