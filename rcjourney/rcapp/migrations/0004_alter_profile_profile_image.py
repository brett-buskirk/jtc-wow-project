# Generated by Django 3.2.9 on 2021-12-10 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcapp', '0003_auto_20211210_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]