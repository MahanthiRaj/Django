from cricket.views import Player1
from django.urls import path

urlpatterns = [
    path('cricket/',Player1, name='Player-1'),
]