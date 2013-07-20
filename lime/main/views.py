# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.forms import UserDataForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError

#=== INPUT ===

def mainView(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
    return render_to_response("main.html", {'user':user}, context_instance=RequestContext(request))

def userProfile(request):
    if request.user.is_authenticated():
        user = request.user
        return render_to_response("profile.html", {'user':user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/")



# falta verificar que el email existe anteriormente. Email unico.
def register(request):
    if request.method=="POST":
        userForm = UserCreationForm(request.POST, prefix="user")
        dataForm = UserDataForm(request.POST, prefix="data")
        if userForm.is_valid():
            if dataForm.is_valid():
                newUser = userForm.save(commit=False)
                newUser.first_name = dataForm.cleaned_data['first_name']
                newUser.last_name = dataForm.cleaned_data['last_name']
                newUser.email = dataForm.cleaned_data['email']
                newUser.save()
#                profile = newUser.profile
#                print dataForm.cleaned_data['category']
#                profile.category = dataForm.cleaned_data['category']
#                profile.save()
#                print newUser.profile.category
                return HttpResponseRedirect("/")
            else:
                return render_to_response("register.html", {'user_form':userForm, 'data_form':dataForm}, context_instance=RequestContext(request))
        else:
            return render_to_response("register.html", {'user_form':userForm, 'data_form':dataForm}, context_instance=RequestContext(request))
    else:
        registerForm = UserCreationForm(prefix="user")
        dataForm = UserDataForm(prefix="data")
        return render_to_response("register.html", {'user_form':registerForm, 'data_form':dataForm}, context_instance=RequestContext(request))        
