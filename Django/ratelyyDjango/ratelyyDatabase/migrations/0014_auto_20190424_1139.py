# Generated by Django 2.1.7 on 2019-04-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0013_auto_20190424_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True),
        ),
    ]
