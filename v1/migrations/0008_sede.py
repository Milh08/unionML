# Generated by Django 3.1.1 on 2020-10-17 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0007_auto_20201014_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('clave', models.CharField(max_length=5)),
                ('clave_ceneval', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('calle', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=30)),
                ('municipio', models.CharField(max_length=30)),
                ('entidad', models.CharField(blank=True, default='CHIAPAS', max_length=30)),
                ('pais', models.CharField(blank=True, default='MÉXICO', max_length=30)),
                ('codigo_postal', models.CharField(max_length=5)),
                ('portal_web', models.CharField(max_length=100)),
                ('correo_electronico', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('extension', models.CharField(max_length=20)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
