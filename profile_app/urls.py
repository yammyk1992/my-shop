from django.urls import path

from profile_app.api.views.profile import ProfileViewSet
from profile_app.views.editprofile import ProfileEdit
from profile_app.views.login import LoginUser
from profile_app.views.logout import logout_user
from profile_app.views.register import Register

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('profile/', ProfileEdit.as_view(), name='profile_account'),
    path('logout/', logout_user, name='logout'),
    path('api/profile', ProfileViewSet.as_view({"get": "list", "post": "create"}), name='api_profile'),
]
