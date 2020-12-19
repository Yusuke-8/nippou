from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    params = {
        'title': 'hello/Index',
        'msg': 'This is sample page.',
        'goto': 'next'
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title': 'hello/Next',
        'msg': 'This is sample page.',
        'goto': 'index'
    }
    return render(request, 'hello/index.html', params)