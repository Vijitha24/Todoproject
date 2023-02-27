from django.shortcuts import render,redirect
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

from django.urls import reverse_lazy

class Tasklistview (ListView):
     model = Task
     template_name = "Home.html"
     context_object_name = "task1"

class Taskdetailview (DetailView):
     model = Task
     template_name = "details.html"
     context_object_name = "task"

class Taskupdateview (UpdateView):
     model = Task
     template_name = "update.html"
     context_object_name = "task"
     fields = ('Name','Priority','Date')

     def get_success_url(self):
          return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview (DeleteView):
     model = Task
     template_name = "delete.html"
     success_url = reverse_lazy('cbvHome')
     fields = ('Name','Priority','Date')
# Create your views here.
def Home(request):
     task1 = Task.objects.all()
     if request.method =="POST":
          Name = request.POST.get('Task','')
          Priority = request.POST.get('Priority','')
          Date= request.POST.get('Date', '')
          task=Task(Name=Name, Priority=Priority,Date=Date)
          task.save()

     return render(request,"Home.html",{'task1':task1})
#
# def details(request):
#
#      return render (request,"details.html")

def delete (request,taskid):
     task=Task.objects.get(id=taskid)
     if request.method == 'POST':
          task.delete()
          return redirect('/')
     return render(request,"delete.html")

def update (request,id):
     task = Task.objects.get(id=id)
     form=TodoForm (request.POST or None, instance=task)
     if form.is_valid():
         form.save()
         return redirect('/')
     return render(request,'edit.html',{'form':form,'task':task})