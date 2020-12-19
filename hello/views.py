from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .form import HelloForm
from .models import Friend


class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'messgae': 'all friends.',
            'data': Friend.objects.all(),
            'form': HelloForm()
            }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        self.params['data'] = [item]
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
    