# Generated by Django 3.0.4 on 2022-07-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='イメージ画像'),
        ),
    ]
