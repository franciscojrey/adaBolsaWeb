# Generated by Django 5.1.4 on 2025-01-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('cuerpo', models.TextField()),
            ],
        ),
    ]
