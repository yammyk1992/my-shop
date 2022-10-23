from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class LoginUser(LoginView):
    """Класс авторизации пользователей"""
    form_class = AuthenticationForm
    template_name = 'profile/login.html'

    # Включаем переадресация для авторизированных пользователей
    redirect_authenticated_user = True

    # Если авторизированны, то куда будет переадресация
    next_page = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')
