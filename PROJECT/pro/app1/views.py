from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import student
from app1.models import employee
from app1.forms import studentform
from app1.forms import employeeform

def home(request):
    d=student.objects.all()
    f=employee.objects.all()
    s=employee.objects.all()
    return render(request,'home.html',{'d':d,'f':f,'s':s})


def index(request):
    return HttpResponse("hello")

#built in forms
def form1(request):
    form=studentform() #for getting form page from admin
    if(request.method=='POST'):
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'form1.html',{'form':form})

#user defined without using objects
def form2(request):
    if(request.method=='POST'):
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'form2.html')

#user defined  using objects
def form3(request):
    if(request.method=='POST'):
        n=request.POST['n']
        m=request.POST['a']
        s=student.objects.create(name=n,age=m)
        s.save()
        return home(request)
    return render(request,'form3.html')

def form4(request):
    if(request.method=='POST'):
        form=employeeform(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'form4.html')


def edit_item(request,p):
    b=employee.objects.get(pk=p)
    form=employeeform(instance=b)
    if(request.method=='POST'):
        form=employeeform(request.POST,instance=b)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'edit.html',{'form':form})


def delete_item(request,p):
    b=employee.objects.get(pk=p)
    b.delete()
    return home(request)
