# Generated by Django 5.1.1 on 2024-10-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0002_alter_source_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='topic_images/default_topic_images.png', upload_to='topic_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='source',
            name='image',
            field=models.ImageField(default='source_images/default_source_images.png', upload_to='source_images/'),
        ),
    ]
