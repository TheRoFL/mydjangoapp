# Generated by Django 4.2 on 2023-05-01 13:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileData',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('preferences', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('interests', models.TextField(max_length=100, validators=[django.core.validators.int_list_validator])),
                ('sexualorientation', models.TextField(max_length=100, validators=[django.core.validators.int_list_validator])),
                ('avatar', models.ImageField(upload_to='avatars')),
            ],
        ),
    ]