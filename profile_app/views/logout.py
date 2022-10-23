from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_user(request):
    """Функция выхода из аккаунта"""
    logout(request)
    return redirect('login')
