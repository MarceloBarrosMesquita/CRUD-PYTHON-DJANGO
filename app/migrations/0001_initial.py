# Generated by Django 4.0.3 on 2022-03-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('curso', models.CharField(max_length=150)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
