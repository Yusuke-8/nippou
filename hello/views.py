from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from .form import FriendForm
from .form import FindForm
from .models import Friend

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

def index(request):
    params = {
        'title': 'hello',
        'create': 'アカウント作成',
        'data': Friend.objects.all()
    }
    return render(request, 'hello/index.html', params)

def create(request):
    params = {
        'title': 'hello',
        'form': FriendForm()
    }
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance = obj)
        friend.save
        return redirect(to='/hello')

    return render(request, 'hello/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    params = {
    'title': 'hello',
    'id': num,
    'form': FriendForm(instance=obj)
    }
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance = obj)
        friend.save
        return redirect(to='/hello')

    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    params = {
    'title': 'hello',
    'id': num,
    'obj': friend
    }
    if (request.method == 'POST'):
        friend.delete
        return redirect(to='/hello')

    return render(request, 'hello/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        # find_id = request.POST['id']
        find = request.POST['name']
        data = Friend.objects.filter(name__contains=find)
        msg = 'Result:' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()

    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data
    }
    return render(request, 'hello/find.html', params)
