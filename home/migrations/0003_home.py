# Generated by Django 3.2.8 on 2021-10-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211008_0423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='home')),
            ],
        ),
    ]
