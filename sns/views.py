from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Message, Friend, Group, Good
from .forms import GroupCheckForm, GroupSelectForm, FriendForm, CreateGroupForm, PostForm

@login_required(login_url='/admin/login')
def index(request, page=1):
    (public_user, public_group) = get_public()

    if request.method == 'POST':
        checkform = GroupCheckForm(request.user, request.POST)
        glist = []
        for item in request.POST.getlist('groups'):
            glist.append(item)
        messages = get_your_group_message(request.user, glist, page)
    else:
        checkform = GroupCheckForm(request.user)
        gps = Group.objects.filter(owner=request.user)
        glist = [public_group.title]
        for item in gps:
            glist.append(item.title)
        messages = get_your_group_message(request, user, glist, page)
        params = {
            'login_user':request.user,
            'contents':messages,
            'check_form':checkform
        }

    return render(request, 'sns/index.html', paramas)

@login_required(login_url='/admin/login/')
def groups(request):
    friends = Friend.objects.filtter(owner=request.user)
    if request.method == 'POST':
        if request.POST['POST'] == '__groups_form__':
            sel_group = request.POST['groups']
            gp = Friend.objects.filter(title=set_group).first()
            fds = Friend.objects.filter(owner=request.user).filter(group=gp)
            print(Friend.objects.filter(owner=request.user))
            vlist = []
            for item in fds:
                vlist.append(item.user.username)
            groupsform = GroupSelectForm(request)