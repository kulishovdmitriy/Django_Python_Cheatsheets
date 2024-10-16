from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import ModelForm

from accounts.models import User, Profile


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user_model = User

        if email and password:
            try:
                user = user_model.objects.get(email=email)
            except user_model.DoesNotExist:
                raise forms.ValidationError("Invalid email or password")

            if not user.check_password(password):
                raise forms.ValidationError("Invalid email or password")

            if not self.user_cache:
                self.confirm_login_allowed(user)

            self.cleaned_data['username'] = user.username
        return super().clean()


class UserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['username', 'last_name', 'first_name', 'email']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'image']
