from http.client import responses
from django.shortcuts import render,redirect
from .models import addteacher,addstudent,addhealth,crud

# Create your views here.

def index(request):
    return render(request,'index.html')

def tlogin(request):
    return render(request,'tlogin.html')

def tlog(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        cr=addteacher.objects.filter(username=username,password=password)
        if cr:
            teacher_details=addteacher.objects.get(username=username,password=password)
            id=teacher_details.id
            department=teacher_details.department
            request.session['id']=id
            request.session['department']=department
            return redirect('thome')
        else:
            return render(request,'tlogin.html')
    else:
        return render(request,'index.html')  
   

def thome(request):
    return render(request,'thome.html')


def addstudents(request):
    if request.method=="POST":
       name=request.POST.get('name')
       sid=request.POST.get('sid')
       email=request.POST.get('email')
       batch=request.POST.get('batch')
       department=request.POST.get('department')
       username=request.POST.get('username')
       password=request.POST.get('password')
       addstudent(name=name,sid=sid,email=email,batch=batch,department=department,username=username,password=password).save()
    return render(request,'addstudents.html')

def slogin(request):
    return render(request,'slogin.html')

def slog(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        cr=addstudent.objects.filter(username=username,password=password)
        if cr:
           user_details=addstudent.objects.get(username=username,password=password)
           id=user_details.id
           sid=user_details.sid
           department=user_details.department

           request.session['sid']=sid
           request.session['department']=department
           request.session['id']=id
           return redirect('shome')
        else:
            return render(request,'slogin.html')
    else:
        return render(request,'index.html')  
   
def shome(request):
    return render(request,'shome.html')


def healthcare(request):
    if request.method=="POST":
       name=request.POST.get('name')
       height=request.POST.get('height')
       weight=request.POST.get('weight')
       bloodgroup=request.POST.get('bloodgroup')
       drinkingwater=request.POST.get('drinkingwater')
       regularperiods=request.POST.get('regularperiods')
       mentalissues=request.POST.get('mentalissues')
       sid=request.POST.get('sid')
       department=request.POST.get('department')
       addhealth(name=name,height=height,weight=weight,bloodgroup=bloodgroup,drinkingwater=drinkingwater,regularperiods=regularperiods,mentalissues=mentalissues,sid=sid,department=department).save()
    return render(request,'addhealth.html')

def viewhealth(request):
    sid=request.session['sid']
    cr=addhealth.objects.filter(sid=sid)
    return render(request,'viewhealth.html',{'cr':cr})

def viewstudent(request):
    department=request.session['department']
    cr = addstudent.objects.filter(department=department)
    return render(request,'viewstudents.html',{'cr':cr})

def crud(request):
    return render(request,'addfile.html')


def viewfile(request,id):
    cr=crud.object.get(id=pk)
    return render(request,'viewfile.html',{'cr':cr})

def addvaccination(request):
    return render(request,'addvaccination.html')

def addfile(request):
    return render(request,'addfile.html')


def tviewhealth(request):
    department=request.session['department']
    cr=addhealth.objects.filter(department=department)
    return render(request,'viewhealth.html',{'cr':cr})







