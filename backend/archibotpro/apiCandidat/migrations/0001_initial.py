# Generated by Django 4.1 on 2022-08-31 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=20)),
                ('resume', models.FileField(blank=True, upload_to='resumes/')),
                ('rendez_vous', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
