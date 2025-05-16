#urls used for defining paths 
#manage .py is the main function it will manage the whole project
#configrations are be done in settings like creatings blocks or sub tasks like patients , dovctors
#whenwver we add any templetes we have to run migrations
#wsgi if we want to run outside locat we keep that server link here here 
#Django have its own inbulit server 
#monoservices diff develops like java, dotnet ,react all can work merge code 
#monilithic means all cide will be there in one place developer work on same langugage (one language - like java or dotnet like that)
#if we want to conncet different sever we go to engine in setting.oy and we chnage the database

from patients.views import Patientlst
from patients.views import patienthtml
from django.urls import path

urlpatterns = [
    path('patients/',Patientlst, name='Patient-lst'),
    path('patient/',patienthtml, name='patitent-html'),
]
