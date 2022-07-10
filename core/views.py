from django.shortcuts import render, redirect
import pandas as pd
from .models import *

# Create your views here.
def uploadDb(path):
    read_csv = pd.read_csv(path, delimiter=',')
    list_csv = [list(row) for row in read_csv.values]

    for item in list_csv:
        Person.objects.create(
            name = item[0],
            email = item[1],
            gender = item[2],
            phone = item[3],
            ip = item[4],
            adress = item[5],
        )

def upload(request):
    if request.method == "POST":
        file = request.FILES['file']
        print(file)
        obj = File.objects.create(file=file)
        print(obj)
        uploadDb(obj.file)

    return render(request, 'upload.html')