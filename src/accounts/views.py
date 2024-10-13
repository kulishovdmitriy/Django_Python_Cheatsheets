from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.edit import ProcessFormView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from accounts.models import User
from accounts.forms import AccountCreateForm, UserUpdateForm, ProfileUpdateForm
from accounts.tasks import send_password_reset_email

# Create your views here.


class AccountRegisterView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = AccountCreateForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        result = super().form_valid(form)
        user = form.instance
        messages.info(self.request,
                      f'Your account "{user.username}" has been successfully created. You can now log in.')
        return result


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


class ProfileUpdateView(LoginRequiredMixin, ProcessFormView):

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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):

    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    html_email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'password_reset_subject.txt'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        send_password_reset_email.delay(email)
        return super().form_valid(form)
