from django.shortcuts import render


def home(request):
    name = 'Bobik'
    return render(request, 'home.html', {'name': name})