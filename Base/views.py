from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,'Index.html')

def Home(request):
    return render(request,'Home.html')

def ENF(request):
    return render(request,'Alert/ENF.html')

def Forbidden(request):
    return render(request,'Alert/Forbidden.html')

def ISE(request):
    return render(request,'Alert/ISE.html')

def SU(request):
    return render(request,'Alert/SU.html')

def WIP(request):
    return render(request,'Alert/WIP.html')