from django.shortcuts import render
from todolist.models import To_do

def t(request):
	list=To_do.objects.all()
	return render(request,'todolist/list.html',{'list':list}) 

# Create your views here.
