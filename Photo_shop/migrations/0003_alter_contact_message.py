# Generated by Django 4.0.2 on 2023-05-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_shop', '0002_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=400),
        ),
    ]