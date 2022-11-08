from django.shortcuts import render
import pickle

def home(request):

    return render(request,'home.html')

def predict(request):
    if request.method == 'POST':
        import numpy as np
        import pandas as pd
        n=float(request.POST.get('n'))
        p=float(request.POST.get('p'))
        k=float(request.POST.get('k'))
        temp=float(request.POST.get('temp'))
        humi=float(request.POST.get('humi'))
        ph=float(request.POST.get('ph'))
        rain=float(request.POST.get('rain'))
        random = pickle.load(open('random_forest.sav','rb'))
        result = random.predict([[n,p,k,temp,humi,ph,rain]])
        return render(request,'result.html',{'crr':result})