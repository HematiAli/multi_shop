# Generated by Django 4.2.5 on 2023-09-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user-image', verbose_name='عکس پروفایل'),
        ),
    ]
