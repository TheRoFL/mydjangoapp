# Generated by Django 4.2 on 2023-05-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0004_alter_message_uploaded_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat_avatar',
            field=models.ImageField(blank=True, null=True, upload_to='chats/avatars/%Y/%m/%d/'),
        ),
    ]