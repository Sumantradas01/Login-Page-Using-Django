from django.shortcuts import redirect, render
from django.http import HttpResponse
from store.models import userdata
def test(request):
    return HttpResponse('Hello, World!')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def registration(request):
    return render(request, 'registration.html')
def signup(request):
    a=userdata()
    a.Name=request.GET['name']
    a.Email=request.GET['email']
    a.Password=request.GET['password']
    a.save()
    return render(request,'registration.html')
def login(request):
    return render(request,'login.html')
def log(request):    
    a=userdata.objects.filter(Email=request.GET['email'],Password=request.GET['password'])
    if a:
        return render(request,'home.html')
    else:
        return render(request,'login.html')


def show(request):
    a=userdata.objects.all()
    return render(request,'show.html',{'data':a})

def delete(request,id):
    a=userdata.objects.get(id=id)   
    a.delete()
    return redirect('/show')

def edit(request,id):
    d=userdata.objects.get(id=id)
    return render(request,'edit.html',{'x':d})

def edcode(request,id):
    d=userdata.objects.get(id=id)
    d.Name=request.GET['Name']
    d.Email=request.GET['Email']
    d.Password=request.GET['Password']
    d.save()
    return redirect('../show')
# Create your views here.

