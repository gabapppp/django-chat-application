# Generated by Django 4.2.4 on 2023-08-19 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0004_chatroom_alter_message_chat_room_delete_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='slug',
        ),
    ]
