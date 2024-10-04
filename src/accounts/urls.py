from django.urls import path

from src.accounts.views import AccountRegisterView, AccountLoginView, AccountLogoutView, ProfileUpdateView


app_name = 'accounts'

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='registration'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/<uuid:uuid>/', ProfileUpdateView.as_view(), name='profile')
]
