# Generated by Django 4.0.2 on 2023-05-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_shop', '0012_alter_contact_email_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.CharField(default='General', max_length=30),
        ),
    ]
