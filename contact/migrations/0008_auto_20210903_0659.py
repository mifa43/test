# Generated by Django 3.2.6 on 2021-09-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_adressentery_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='person',
        ),
        migrations.AddField(
            model_name='adressentery',
            name='firstName',
            field=models.CharField(default='a', max_length=120),
        ),
        migrations.AddField(
            model_name='adressentery',
            name='lastName',
            field=models.CharField(default='z', max_length=120),
        ),
        migrations.AddField(
            model_name='adressentery',
            name='phoneNumber',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
