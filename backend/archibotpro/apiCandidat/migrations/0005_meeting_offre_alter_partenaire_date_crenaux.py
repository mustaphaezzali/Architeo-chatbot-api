# Generated by Django 4.1 on 2022-09-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiCandidat', '0004_remove_candidat_rendez_vous_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('details', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type_contrat', models.CharField(max_length=100)),
                ('salaire', models.IntegerField(blank=True, null=True)),
                ('entreprise', models.CharField(max_length=100)),
                ('mode', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='partenaire',
            name='date_crenaux',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]