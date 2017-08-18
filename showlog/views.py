
# coding=utf8
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from django.utils.timezone import now, timedelta
import datetime
import time
from django.db.models import Q
from collections import OrderedDict
import random
from collections import deque
import json
from .models import User
from .models import Host
from .models import Table
from .models import Usergroup
from .Totype import *
import base64
def index(request):
    return render(request,'index.html')

def usergroupget(request):
    usergroup=AllUsergroup()
    return render(request,'usergroup.html',{'usergroup':usergroup})

def userget(request):
    user=AllUser()
    return render(request,'user.html',{'user':user})

def hostget(request):
    host=AllHost()
    return render(request,'host.html',{'host':host})

def mistakelogshow(request):
    table=AllTable()
    return render(request, 'mistakelogshow.html', {'table': table})

def setting(request):
    if request.GET['ip']:
        configs=FindHost(request.GET['ip'])
        return HttpResponse(configs[0].services[1])
    return HttpResponse()

def testapi(request):
    if 'table' in request.POST:
        SaveTable(request.POST)
    return HttpResponse()

def logshow(request):
    return render(request,'logshow.html')