# Generated by Django 3.2.6 on 2021-08-25 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0004_adressentery_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adressentery',
            name='user',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adressentery', to=settings.AUTH_USER_MODEL),
        ),
    ]
