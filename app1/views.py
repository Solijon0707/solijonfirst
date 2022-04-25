from django.shortcuts import render , redirect

from translate import Translator
from .models import *
# Create your views here.


# pip install translate  3.6.1
def home(request):
    return render(request,'1.html')

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        newtask = Task(task = request.POST['text'])
        newtask.save()
        return redirect('/app1/todo/')
    return render(request, 'index.html', {'tasks': tasks})

def edit1(request,id):
    task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    if request.method == 'POST':
        task.task = request.POST['text']
        task.save()
        return redirect('/app1/todo/')
    return render(request,'index1.html',{'task':task,'tasks':tasks,})

def delete1(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/app1/todo/')


def ad(request):
    result1 = 0
    a=0
    b=0
    d=0
    if request.method == 'POST':
        a=request.POST['int1']
        b=request.POST['int2']
        if request.POST['qosh'] == 'qqq':
            result1 = int(request.POST['int1']) + int(request.POST['int2'])
            d=f'{a}+{b}'
        elif request.POST['qosh']=='ayr':
            result1 = int(request.POST['int1']) - int(request.POST['int2'])
            d=f'{a}-{b}'
        elif request.POST['qosh']=='kop':
            result1 = int(request.POST['int1']) * int(request.POST['int2'])
            d=f'{a}*{b}'
        elif request.POST['qosh']=='bol':
            result1 = int(request.POST['int1']) / int(request.POST['int2'])
            d=f'{a}/{b}'
    return render(request,'calculator.html', {'result1': result1,'a':a,'b':b,'d':d})



def translat(request):
    b=a=c=''
    if request.method=='POST':
        # translator = Translator(to_lang='uz', from_lang='ru')
        a=request.POST['text']
        # b=translator.translate(a)
        b=Translator(to_lang='uz', from_lang='en').translate(a)
        c=Translator(to_lang='ru', from_lang='en').translate(a)
    return render(request,'translate.html',{'b':b,'a':a,'c':c})
