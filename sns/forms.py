from django import forms
from .models import Message, Group, Friend, Good
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['owner', 'group', 'content']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['owner', 'title']

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['owner', 'user', 'group']

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['owner', 'message']

class GroupCheckForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(GroupCheckForm, self).__init__(*args, **kwargs)
        public = User.objects.filter(username='public').first()
        self.fields['group'] = forms.MultipleChoiceField(
            choices = [(item.title, item.title) for item in Group.objects.filter(owner__in=[user,public])],
            widget = forms.CheckboxSelecterMultiple(),
        )

class GroupSelectForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(GroupSelectForm, self).__init__(*args, **kwargs)
        self.fields['freinds'] = forms.ChoiceField(
            choices = [('-','-')] + [(item.title, item.title) for item in Group.objects.filter(owner=user)],
            widget = forms.Select(attr={'class':'form-control'})
        )

class FriendForm(forms.Form):
    def __init__(self, user, friend=[], vals=[], *args, **kwargs):
        super(FriendForm, self).__init__.(*args, **kwargs)
        self.friends['friend'] = forms.MultipleChoiceField(
            choices=[(item.user, item.user) for item in friends],
            widget=forms.CheckboxSelecterMultiple(),
            initial=vals
        )

class CreateGroupForm(forms.Form):
    group_name = forms.CharField(max_length=50,widget=forms.TextInput(attr={'class':'form-control'}))

class PostForm(forms.Form):
    content = forms.CharField(max_length=500, widget=forms.Textarea(attr={'class':'form-control', 'row':2}))

    def __init__(self, user *args, **kwargs):
        pubcil = User.objects.filtter(username='public').first()
        self.fields['group'] = forms.ChoiceField(choices[('-','-')] + [(item.title, item.title) for item in Group.objects],widget= forms.Select(attr={'class':'form-control'}))