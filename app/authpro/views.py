from django.shortcuts import render


def register(request):
    return render(request, 'authpro/register.html')


def login(request):
    return render(request, 'authpro/login.html')
