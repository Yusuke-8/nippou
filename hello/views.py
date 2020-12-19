from django.shortcuts import render
from django.http import HttpResponse
from .form import HelloForm

# Create your views here.
def index(request):
    params = {
        'title': 'hello/Index',
        'message': 'your data:',
        'form': HelloForm(),
        'goto': 'next'
    }
    if (request.method == 'POST'):
        params['message'] = '名前:' + request.POST['name'] + \
                            '<br>メール:' + request.POST['mail'] + \
                            '<br>年齢:' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title': 'hello/Next',
        'msg': 'This is sample page.',
        'goto': 'index'
    }
    return render(request, 'hello/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title': 'Hello/Form',
        'msg': 'Hello '+ msg + '.' ,
        'goto': 'index'
    }
    return render(request, 'hello/index.html', params)