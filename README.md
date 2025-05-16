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
step-11: created an HTML template under patients
step-12: created a view function that renders an HTML page using Django -> template.loader

          from django.template import loader

          def patienthtml(request):
              template = loader.get_template('patients.html')
              return HttpResponse(template.render())
step -12: Then connected the patienthtml view to a URL to get access the browser 

          from patients.views import patienthtml
          from django.urls import path
          
          urlpatterns = [
                      path('patient/',patienthtml, name='patitent-html'),
                    
          ] 
setp-13: Then we run the server to check the expected output
step-14: created models in Django to store information about patients and doctors in the database. 
          Django ORM helps turn these models into database tables automatically
          
          from django.db import models

          class patients(models.Model):
              firstname = models.CharField(max_length = 255)
              lastname = models.CharField(max_length = 255)
          
          class doctors(models.Model):
              firstname = models.CharField(max_length = 255)
              lastname = models.CharField(max_length = 255)
          

step-15:Then we run this command 

          python manage.py makemigrations

          This tells Django to get ready to create the database tables

step-16: Finally Django will check the models and it will create migration file 

          class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
    ]

