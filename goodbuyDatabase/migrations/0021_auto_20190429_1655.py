# Generated by Django 2.1.7 on 2019-04-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodbuyDatabase', '0020_auto_20190429_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='anm_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='env_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='hmn_description',
            field=models.TextField(null=True),
        ),
    ]