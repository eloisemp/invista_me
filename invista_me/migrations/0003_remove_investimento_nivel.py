# Generated by Django 5.0.6 on 2024-06-17 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0002_investimento_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investimento',
            name='nivel',
        ),
    ]
