from django.shortcuts import render


def home(request):
    name = "Bob"

    return render(request, 'home.html', context={"name": name})

def about(request):
    name = "About us"

    return render(request, 'about.html', context={"name": name})
