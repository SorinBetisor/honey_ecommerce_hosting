# Generated by Django 2.2.13 on 2022-03-12 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]