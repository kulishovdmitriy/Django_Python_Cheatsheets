from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.edit import ProcessFormView
from django.http import HttpResponseRedirect

from accounts.models import User
from accounts.forms import AccountCreateForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


class AccountRegisterView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = AccountCreateForm
    success_url = reverse_lazy('core:index')


class AccountLoginView(LoginView):
    template_name = 'login.html'

    def get_redirect_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return reverse('core:index')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.info(self.request, f'User {self.request.user} has been successfully logged in')
        return result


class AccountLogoutView(LogoutView):
    template_name = 'logout.html'


class ProfileUpdateView(ProcessFormView):

    def get_object(self):
        # Получаем UUID из kwargs
        uuid = self.kwargs.get('uuid')
        # Находим пользователя по UUID
        user = get_object_or_404(User, uuid=uuid)
        return user

    def get(self, request, *args, **kwargs):

        user = self.get_object()
        profile = self.request.user.profile

        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

        return render(
            request=request,
            template_name='profile.html',
            context={
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )

    def post(self, request, *args, **kwargs):

        user = self.get_object()
        profile = self.request.user.profile

        user_form = UserUpdateForm(data=request.POST, instance=user)
        profile_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(self.request, 'The profile is successfully changed')
            return HttpResponseRedirect(reverse('accounts:profile', kwargs={'uuid': str(user.uuid)}))

        return render(
            request=request,
            template_name='profile.html',
            context={
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )
