from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    subjects = Subject.objects.all()
    context = {
    'subjects': subjects,
    }
    return render(request, 'subjects/index.html', context)

def classes(request):
    classes = Class.objects.all()
    context = {
    'classes': classes,
    }
    return render(request, 'subjects/classes.html', context)

def newclass(request):
    if request.method == 'POST':
        name = request.POST['classname']
        newclass =  Class(name = name)
        newclass.save()
        return redirect('subjects:classes')
    else:
        return render(request, 'subjects/newclass.html')

def newsubject(request):
    if request.method == 'POST':
        subjectcode = request.POST['subjectcode']
        subjectname = request.POST['subjectname']
        _class = request.POST['_class']
        if Subject.objects.filter(code = subjectcode).exists():
            messages.error(request, 'Subject Already Exists')
            return redirect('subjects:newsubject')
        else:
            subject = Subject(code = subjectcode, name = subjectname, _class_id = _class)
            subject.save()
            return redirect('subjects:index')
    else:
        classes = Class.objects.all()
        if classes:
            context = {
            'classes': classes,
            }
            return render(request, 'subjects/newsubject.html', context)
        else:
            return redirect('subjects:newclass')
