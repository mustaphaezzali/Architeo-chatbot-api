# Generated by Django 4.1 on 2022-09-01 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiCandidat', '0002_client_partenaire_recruteur_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidat',
            old_name='rendez_vous_day',
            new_name='rendez_vous',
        ),
    ]