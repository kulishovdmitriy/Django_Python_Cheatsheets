# Generated by Django 5.1.1 on 2024-09-30 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['title']},
        ),
    ]
