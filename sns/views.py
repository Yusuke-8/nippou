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