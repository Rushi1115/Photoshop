# Generated by Django 4.0.2 on 2023-05-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_shop', '0004_alter_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
    ]
