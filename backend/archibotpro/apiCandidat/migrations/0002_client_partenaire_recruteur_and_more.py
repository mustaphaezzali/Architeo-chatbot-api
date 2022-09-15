# Generated by Django 4.1 on 2022-09-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiCandidat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('service', models.CharField(max_length=30)),
                ('telephone', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('appel_telephonique', models.BooleanField(default=False)),
                ('piece_jointe', models.FileField(blank=True, upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('type_partenariat', models.CharField(blank=True, max_length=200)),
                ('telephone', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('appel_telephonique', models.BooleanField(default=False)),
                ('date_crenaux', models.DateTimeField(blank=True)),
                ('piece_jointe', models.FileField(blank=True, upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Recruteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('entreprise', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=200)),
                ('needed_profile', models.CharField(blank=True, max_length=200)),
                ('appel_telephonique', models.BooleanField(default=False)),
                ('piece_jointe', models.FileField(blank=True, upload_to='documents/')),
            ],
        ),
        migrations.RenameField(
            model_name='candidat',
            old_name='rendez_vous',
            new_name='rendez_vous_day',
        ),
        migrations.AddField(
            model_name='candidat',
            name='adress',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='candidat',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='candidat',
            name='niveau_etudes',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='candidat',
            name='telephone',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
