import json
import copy
import time
import base64
from .models import User
from .models import Host
from .models import Table
from .models import Usergroup
from collections import deque

def AllUsergroup():
    usergroup=Usergroup.objects.all()
    return JsonUsergroup(usergroup)

def FindUsergroup(Id):
    usergroup = Usergroup.objects.filter(id=Id)
    return JsonUsergroup(usergroup)

def AllUser():
    user=User.objects.all()
    return  JsonUser(user)

def FindUser(Id):
    user=User.objects.filter(id=Id)
    return JsonUser(user)

def AllHost():
    host=Host.objects.all()
    return JsonHost(host)

def FindHost(Ip):
    host=Host.objects.filter(Host=Ip)
    return JsonHost(host)

def AllTable():
    table=Table.objects.all()
    #print type()
    for x in range(0,len(table)):
        table[x].sendtime=time.strftime("%Y %b %d %H:%M:%S", time.localtime(int(table[x].sendtime)))
        table[x].date=base64.b64decode(table[x].date)

    return table

def JsonUser(user):
    user_bak=user
    x=deque()
    for y in range(0,len(user_bak)):
        if  user_bak[y].userhost:
            for keys in eval(user_bak[y].userhost)['host'].keys():
                x.append(eval(user_bak[y].userhost)['host'][keys])
            user[y].userhost=",".join(x)
            x.clear()
    return user

def JsonUsergroup(usergroup):
    usergroup_bak=usergroup
    x=deque()
    for y in range(0,len(usergroup_bak)):
        if usergroup_bak[y].username:
            for keys in eval(usergroup_bak[y].username)['user'].keys():
                x.append(eval(usergroup_bak[y].username)['user'][keys])
            usergroup[y].username=",".join(x)
            x.clear()
    return usergroup

def JsonHost(host):
    host_bak = host
    x = deque()
    z = deque()
    for y in range(0, len(host_bak)):
        if host_bak[y].services:
            for keys in eval(host_bak[y].services)['service'].keys():
                # x.append(eval(host_bak[y].services)['service'][keys])
                z.append(keys)
            x.append(",".join(z))
            x.append(host_bak[y].services)
            host[y].services = copy.copy(x)
            x.clear()
    return host

def SaveTable(POST):
    tabledict = json.loads(POST['table'].replace("u", "", 1).replace("'", '"'))
    for keys in tabledict:
        service = keys
        HostIp = tabledict[keys][0]
        date = tabledict[keys][1]
        sendtime = int(tabledict[keys][2])
        for x in date:
            Table.objects.create(hostip=HostIp, service=service, date=x, sendtime=sendtime)
        # print(service, HostIp, sendtime)
