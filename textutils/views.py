from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    return render(request,'analyze.html')
def iop(request):
    return render(request,"kok.html")

def ahmad(request):
    return render(request,'bootstrap.html')

def goo(request):
    t=request.POST.get('text','default')
    f=request.POST.get('doy','default')

    d={'kol':t,'ft':f}
    send_mail('ahmad',t,settings.EMAIL_HOST_USER,['2020ce12@student.uet.edu.pk'],fail_silently=False)

    return render(request,'index.html',d)

def removepun(request):
    t=request.POST.get('text','default')
    if t=='':
        return HttpResponse("Error")

    r=request.POST.get('removepun','off')
    u=request.POST.get('capital','off')
    e=request.POST.get('ool','off')
    n=request.POST.get('newlineremover','off')
    s=''
    p='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    pop=''

    if r=='on':
        for i in t:
            if i not in p:
                s = s + i
        pop=pop+"-Remove puntuation"
        t=s
    if u =='on' :
        y=t.upper()
        t=y
        pop=pop+"-Capitalize"
    if e== 'on' :
        d=''
        for index,char in enumerate(t):
            if not (t[index] == ' ' and t[index+1] == ' '):
                d=d+char
        t=d
        pop=pop+'-Extra space remover'
    if n=='on':
        q =''
        for i in t:
            if i!='\n' and i !='\r':
                q=q+i
        t=q
        pop=pop+'-new line remover'
    uio = {'pop': pop, 'tot': t}
    return render(request, 'analyze1.html', uio)

