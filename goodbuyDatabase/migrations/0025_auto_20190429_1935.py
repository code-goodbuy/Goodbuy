# Generated by Django 2.1.7 on 2019-04-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodbuyDatabase', '0024_auto_20190429_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='animals_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='environment_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='humans_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
