# Generated by Django 3.1.1 on 2020-10-25 21:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0009_auto_20201018_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='direccion',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='direccion',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
