# Generated by Django 3.2.6 on 2021-08-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adressentery',
            name='birthDate',
            field=models.DateField(blank=True),
        ),
    ]
