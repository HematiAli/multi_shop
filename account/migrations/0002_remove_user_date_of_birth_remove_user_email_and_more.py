# Generated by Django 4.2.5 on 2023-09-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=1, max_length=11, unique=True, verbose_name='شماره تلفن'),
            preserve_default=False,
        ),
    ]