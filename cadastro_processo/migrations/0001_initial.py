# Generated by Django 3.1.3 on 2020-11-27 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cliente', models.CharField(max_length=50)),
                ('arquivo', models.FileField(upload_to='')),
            ],
        ),
    ]
