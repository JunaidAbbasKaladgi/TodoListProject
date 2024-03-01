from django.shortcuts import render,HttpResponseRedirect
from .models import taskTable

def TodoList(request):
    if request.method=="POST":
        Tasktitle=request.POST['Tasktitle']
        Taskdesc=request.POST['Taskdesc']
        taskTable.objects.create(Tasktitle=Tasktitle,Taskdesc=Taskdesc)
    return render(request,'Home.html',)

def Tasks(request):
    data=taskTable.objects.all()
    return render(request,'Tasks.html',{'data':data})

def update_Task(request,id):
    data=taskTable.objects.get(id=id)
    if request.method=="POST":
        Tasktitle=request.POST['Tasktitle']
        Taskdesc=request.POST['Taskdesc']
        data.Tasktitle=Tasktitle
        data.Taskdesc=Taskdesc
        data.save()
        return HttpResponseRedirect('/Tasks/')
    return render(request,'updateTask.html',{'data':data})

def delete_Task(request,id):
    data= taskTable.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/Tasks/')