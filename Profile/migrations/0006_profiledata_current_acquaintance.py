# Generated by Django 4.2 on 2023-05-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_profiledata_acquaintances_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledata',
            name='current_acquaintance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]