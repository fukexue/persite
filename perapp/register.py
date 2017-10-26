from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


def registerindex(request):
    return render(request, 'register.html')


def registerresult(request):
    context = {}
    errors = []
    account = None
    password = None
    password2 = None
    email = None
    CompareFlag = False

    if request.method == 'POST':
        if not request.POST.get('user'):
            errors.append('Please Enter user')
        else:
            account = request.POST.get('user')
        if not request.POST.get('password'):
            errors.append('Please Enter password')
        else:
            password = request.POST.get('password')
        if not request.POST.get('secondpassword'):
            errors.append('Please Enter second password')
        else:
            password2 = request.POST.get('secondpassword')
        if not request.POST.get('email'):
            errors.append('Please Enter email')
        else:
            email = request.POST.get('email')

        if password is not None and password is not None:
            if password == password2:
                CompareFlag = True
            else:
                errors.append('password2 is diff password ')

        if account is not None and password is not None and password2 is not None and email is not None and CompareFlag:
            user = User.objects.create_user(account, email, password)
            user.is_active = True
            user.save()
            context['registerflag'] = 1
            return render(request, 'loginindex.html', context)

    return render_to_response('register.html', {'errors': errors})
