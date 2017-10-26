from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, models, logout
from django.http import HttpResponse, HttpResponseRedirect
from perapp.models import PersonalAbstract, OlineProject, OlineNote
# Create your views here.


def mainindex(request):
    context = {}
    nowloginstatus = request.user.is_authenticated()
    if nowloginstatus:
        nowloginuser = request.user.username
    else:
        nowloginuser = 0
    context['nowloginuser'] = nowloginuser
    for personalabstract in PersonalAbstract.objects.all():
        context['personalabstract'] = personalabstract
    for olinenote in OlineNote.objects.all():
        context['olinenote'] = olinenote
    for olineproject in OlineProject.objects.all():
        context['olineproject'] = olineproject
    return render(request, 'mainindex.html', context)


def noteindex(request):
    context = {}
    nowloginstatus = request.user.is_authenticated()
    if nowloginstatus:
        nowloginuser = request.user.username
    else:
        nowloginuser = 0
    context['nowloginuser'] = nowloginuser
    return render(request, 'noteindex.html', context)


def loginindex(request):
    return render(request, 'loginindex.html')


def loginresult(request):
    if request.POST:
        username = request.POST.get("user")
        password = request.POST.get("password")
        print(username)
        print(password)
        if username is not None and password is not None:
            userresult = authenticate(username=username, password=password)
            print("exit 1")
            if userresult is not None:
                print("exit")
                login(request, userresult)
                return HttpResponseRedirect("/mainindex/")
    return render(request, 'loginindex.html')


def projectindex(request):
    context = {}
    nowloginstatus = request.user.is_authenticated()
    if nowloginstatus:
        nowloginuser = request.user.username
    else:
        nowloginuser = 0
    context['nowloginuser'] = nowloginuser
    return render(request, 'projectindex.html', context)


def messageindex(request):
    context = {}
    nowloginstatus = request.user.is_authenticated()
    if nowloginstatus:
        nowloginuser = request.user.username
    else:
        nowloginuser = 0
    context['nowloginuser'] = nowloginuser
    return render(request, 'messageindex.html', context)


def loginout(request):
    logout(request)
    return HttpResponseRedirect("/mainindex")
