# Generated by Django 2.1.7 on 2019-05-12 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0030_auto_20190508_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
