import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

# Create your models here.


def user_directory_path(instance, filename):
    # File save in MEDIA_ROOT/user_<uuid>/<filename>
    return 'user_{0}/{1}'.format(instance.user.uuid, filename)


class User(AbstractUser):

    class USER_ACTION(models.IntegerChoices):
        LOGIN = 0, "Login"
        LOGOUT = 1, "Logout"
        CHANGE_PASSWORD = 2, "Change Password"
        CHANGE_PROFILE = 3, "Change Profile"
        CHANGE_PROFILE_IMAGE = 4, "Change Profile image"

    uuid = models.UUIDField(null=True, default=uuid.uuid4)
    action = models.PositiveSmallIntegerField(choices=USER_ACTION.choices, default=USER_ACTION.LOGIN)


class Profile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(validators=[MinLengthValidator(10)], max_length=10, null=True)
    image = models.ImageField(default='profile/default.png', upload_to=user_directory_path, null=True)
