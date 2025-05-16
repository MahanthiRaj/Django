from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def Patientlst(request):
    return HttpResponse("Details of thr patent will be displayed here")
def patienthtml(request):
    template = loader.get_template('patients.html')
    return HttpResponse(template.render())



