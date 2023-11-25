# crime_reporting/views.py

from django.shortcuts import render, redirect
from .models import crimereport

def report_crime(request):
    if request.method == 'POST':
         incidentType =request.POST['incidenttype']
         description = request.POST['description']
         yourcontactinformation= request.POST['contactinfo']
         location = request.POST['location']
         
         crimedata=crimereport(incidenttype=incidentType,description=description,yourcontactinformation=yourcontactinformation,location=location)
         crimedata.save()
    return render(request, 'report.html', {})
