# Generated by Django 5.0.1 on 2024-01-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='items',
            name='text',
            field=models.CharField(default=None, max_length=300),
        ),
    ]