# Generated by Django 4.0.2 on 2022-02-20 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usermovie',
            unique_together={('user', 'movie')},
        ),
    ]
