# Django

step-1 :created a repository named  Django.

step-2: created a virtual environment using the following command

          python -m venv env
          
step-3: activates the environment

          env\Scripts\activate
step-4: after activation ,Installed Django

          pip install django
step-5: created a Django project - Health

          django-admin startproject Health
step-6: under Health project created a subapp - Patients:

          python manage.py startapp Patients
step-7: Create Views in views.py

          from django.shortcuts import render
          from django.http import HttpResponse
          def Patientlst(request):
              return("Details of thr patent will be displayed here")

step-8: created a urls.py file inside the Patients app and added the URL patterns 

          from patients.views import Patientlst
          from django.urls import path
          
          urlpatterns = [
              path('patients/',Patientlst, name='Patient-lst'),
          ]

step-9: added the Patients app URLs in the main project- Health->urls.py

          from django.contrib import admin
          from django.urls import path , include
          
          urlpatterns = [
              path('admin/', admin.site.urls),
              path('', include('patients.urls'))
          ]
step-10: Finally i ran the server to test the project locally

          python manage.py runserver

          http://127.0.0.1:8000/patients/
