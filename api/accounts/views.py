from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import JsonResponse

User = get_user_model()


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return JsonResponse({'message': 'Success', 'redirect': reverse('index')})
        else:
            return JsonResponse({'message': 'Invalid credentials'})

    title = "Connexion"
    context = {
        "title": title
    }
    return JsonResponse({'html': render(request, "accounts/login.html", context).content.decode('utf-8')})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)

        login(request, user)
        return JsonResponse({'message': 'Success', 'redirect': reverse('index')})

    title = "S'inscrire"
    context = {
        "title": title
    }
    return JsonResponse({'html': render(request, "accounts/signup.html", context).content.decode('utf-8')})


def logout_user(request):
    logout(request)
    return JsonResponse({'message': 'Success', 'redirect': reverse('index')})
