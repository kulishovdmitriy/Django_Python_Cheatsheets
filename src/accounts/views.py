from django.shortcuts import render, get_object_or_404  # noqa
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse

from accounts.models import User
from accounts.forms import AccountCreateForm, ProfileUpdateForm


# Create your views here.


class AccountRegisterView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = AccountCreateForm
    success_url = reverse_lazy('core:index')


class AccountLoginView(LoginView):
    template_name = 'login.html'

    def get_redirect_url(self):
        return reverse('core:index')


class AccountLogoutView(LogoutView):
    template_name = 'logout.html'


class ProfileUpdateView(UpdateView):
    model = User
    template_name = 'profile.html'
    form_class = ProfileUpdateForm
    pk_url_kwarg = 'uuid'

    def get_object(self, queryset=None):
        uuid = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(User, uuid=uuid)
