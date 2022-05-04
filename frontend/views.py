from django.shortcuts import render

from django.http import HttpResponse
import pandas as pd
from frontend.models import developers,history

def index(request):

    data1 = [28, 48, 40, 19, 95, 27, 55, 33]
    data2 = [30, 22, 17, 48, 0, 28, 30, 20]
    data3 = ['version_1 d1', 'version_1 d2', 'version_1 d3', 'version_1 d4',
             'version_1 d5', 'version_1 d6', 'version_1 d7', "version_8 (Current)"]
    dataHistory=history.objects.all()
    dataHistoryList=[]
    for d in dataHistory:
        dataHistoryList.append( d.search_text)
    print(dataHistoryList)
    return render(request, "index.html", context={"data": [data1, data2, data3,dataHistoryList]})


def stats(request):
    data = [1, 1, 1]
    return render(request, "stats.html", context={"data": data})


def about(request):
    data=developers.objects.all()
    arr=[]
    for d in data:
        dictionary={}
        dictionary["name"]=d.name
        dictionary["path"]=d.path
        dictionary["updated_date"]=d.updated_date
        dictionary["likes"]=d.likes
      
        arr.append(dictionary)
        
    # Nagdatt = {"name": "Nagdatt Gajjam"}
    # Samarth = {"name": "Samarth Kalshetti"}
    # Mahesh = {"name": "Mahesh Vinnu"}
    # Rohan = {"name": "Rohan Pengonda"}
    # Shravani = {"name": "Shravani Kairamkonda"}
    # Shruti = {"name": "Shruti Salunkhe"}
    return render(request, "about.html", context={
        "data": arr
    })


def contact(request):
    return render(request, "contact.html")

# Other Services


def data_analysis_tool(request):
    return render(request, 'dat_index.html')
