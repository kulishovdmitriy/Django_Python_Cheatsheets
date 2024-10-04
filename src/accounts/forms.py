from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import User


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['username', 'last_name', 'first_name', 'email']
