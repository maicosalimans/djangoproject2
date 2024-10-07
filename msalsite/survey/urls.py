from django.urls import path
from . import views

app_name= 'survey'
urlpatterns = [
    path('survey/', views.poll_view, name='poll')
]
