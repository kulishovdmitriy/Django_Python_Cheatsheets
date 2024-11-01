# Generated by Django 5.1.1 on 2024-10-04 20:43

import accounts.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='action',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Login'), (1, 'Logout'), (2, 'Change Password'), (3, 'Change Profile'), (4, 'Change Profile image')], default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('image', models.ImageField(default='profile/default.png', null=True, upload_to=accounts.models.user_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
