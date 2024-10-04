import uuid
from django.db import models # noqa
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    uuid = models.UUIDField(null=True, default=uuid.uuid4)
