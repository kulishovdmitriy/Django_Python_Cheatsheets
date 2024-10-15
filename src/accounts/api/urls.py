from django.urls import path

from accounts.api.views import UserRegistrationAPIView, LogoutAPIView, ProfileAPIView


app_name = 'auth'

urlpatterns = [

    path('signup', UserRegistrationAPIView.as_view(), name='signup'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('profile/<int:id>/', ProfileAPIView.as_view(), name='profile')

]
