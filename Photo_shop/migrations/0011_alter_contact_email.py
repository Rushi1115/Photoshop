# Generated by Django 4.0.2 on 2023-05-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_shop', '0010_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='hey', max_length=50),
        ),
    ]
