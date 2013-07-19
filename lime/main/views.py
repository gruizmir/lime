# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import uuid
from django.contrib.auth.models import User

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
