from django.contrib.auth import login
from django.shortcuts import render, redirect

from django.views import View

from profile_app.forms.registerform import RegisterUserForm


class Register(View):
    """Класс регистрации пользователя"""

    @staticmethod
    def get(request):

        if request.user.is_authenticated:
            return redirect('home')

        form = RegisterUserForm()

        context = {
            'title': 'Регистрация ',
            'form': form
        }
        return render(request, 'profile/register.html', context)

    @staticmethod
    def post(request):
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('home')
        context = {
            'title': 'Registration',
            'form': form,
        }
        return render(request, 'profile/register.html', context)
