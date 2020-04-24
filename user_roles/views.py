# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import PermohonanForm
from .models import Permohonan
from django.http import HttpResponse
from django.contrib.auth.models import Group, User

# Create your views here.
def index(request):
    return render(request, 'user_roles/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if request.POST.get("usertype","") == 'Staff':
            my_group = Group.objects.get(name='Staff') 
            if form.is_valid():
                form.save()
                userid = form.cleaned_data['username']
                name = User.objects.all().filter(username=userid)
                for u in name:
                    my_group.user_set.add(u)
                return redirect('login')
        else:
            my_group = Group.objects.get(name='Contractor') 
            if form.is_valid():
                form.save()
                userid = form.cleaned_data['username']
                name = User.objects.all().filter(username=userid)
                for u in name:
                    my_group.user_set.add(u)
                return redirect('login')

    else:
        form = UserCreationForm()
    
    context = {'form' : form}
    return render(request, 'registration/register.html', context)

def enterpage(request):
    if request.user.has_perm('user_roles.can_submit') :
        name = request.user.username
        reqs = Permohonan.objects.all().filter(contractor=name)
        return render(request, 'pages/contractorpage.html', {'reqs':reqs})
    else:
        reqs = Permohonan.objects.all().filter(request_status='P')
        approved = Permohonan.objects.all().filter(request_status='L')
        args = {'reqs':reqs , 'approved':approved}
        return render(request, 'pages/staffpage.html', args)
        

def PermohonanNew(request):
    form = PermohonanForm( request.POST or None, initial ={'contractor': request.user.username})
    if form.is_valid():
        form.save()
        return redirect('enterpage')

    context = {
        'form': form
    }
    return render(request, 'pages/newform.html', context)

def approvebutton(request):
    reqID = request.GET.get('id')
    Permohonan.objects.filter(id=reqID).update(request_status='L')
    return HttpResponse(render(request, 'pages/changes.html'))

def rejectbutton(request):
    reqID = request.GET.get('id')
    Permohonan.objects.filter(id=reqID).update(request_status='T')
    return HttpResponse(render(request, 'pages/changes.html'))
