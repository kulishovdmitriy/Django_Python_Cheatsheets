from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from accounts.models import User, Profile


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class UserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['last_name', 'first_name', 'email']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'image']
