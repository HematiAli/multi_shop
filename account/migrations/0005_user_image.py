# Generated by Django 4.2.5 on 2023-09-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user-image', verbose_name='عکس کاربر'),
        ),
    ]
