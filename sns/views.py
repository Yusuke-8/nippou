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
            groupsform = GroupSelectForm(request, user, request.POST,)
            friendsform = FriendForm(request.user, friendsform=friends, vals=vlist)

    if  request.POST['mode'] == '__friend_form__':
        sel_group = request.POST['group']
        group_obj = Group.objects.filter(title=sel_group).first()
        print(group_obj)
        sel_fds = request.POST.getlist('friends')
        sel_users = User.objects.filter(username__in=sel_fds)
        fds = Friend.objects.filter(owner=request.user).filter(user__in=sel_users)
        vlist = []
        for item in fds:
            item.group = group_obj
            item.save()
            vlist.append(item.user.username)
        message.success(request, ' チェックされたFriendを' + sel_group + 'に登録しました。')
        groupsform = GroupSelectForm(request.user, {'group':sel_group})
        friendsform = FriendsForm(request.user, friends=friends, vals=vlist)
    else:
        groupsform = GroupSelectForm(request.user)
        friendsform = FriendForm(request.user, friends=friends, vals=[])
        sel_group = '-'

    createform = CreateGroupForm()
    params = {
        'login_user':request.user,
        'group_form':groupform,
        'friends_form':FriendsForm,
        'create_form':createform,
        'group':sel_group,
    }
    return render(request, 'sns/groups.html', params)

