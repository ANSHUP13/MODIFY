# i have created this file - Anshuman.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index2.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def analyse(request):
    def capfrist(t):
        return t.capitalize()
    def countchar(t):
        return len(t)
    def removepunc(t):
        s = ''
        for j in t:
            if j.isalnum():
                s = s+j
        return s
    def spaceremover(t):
        t.strip()
        s = ''
        for i in t:
            if i != ' ':
                s = s+i
        return s
    t = request.POST.get('text','default')
    rp = request.POST.get('remonvepunc','off')
    cf = request.POST.get('capfirst','off')
    sr = request.POST.get('spaceremover','off')
    cc = request.POST.get('countchar','off')
    if sr == 'on':
        t = spaceremover(t)
    if cf == 'on':
        t = capfrist(t)
    if rp == 'on':
        t = removepunc(t)
    n = 'not checked'
    if cc == 'on':
        n = countchar(t)
    param = {'t':t,'n':n}
    return render(request,'analyse2.html',param)