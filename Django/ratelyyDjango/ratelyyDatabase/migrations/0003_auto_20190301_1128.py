# Generated by Django 2.1.7 on 2019-03-01 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0002_auto_20190301_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Company'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='concern',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Concern'),
        ),
        migrations.AlterField(
            model_name='company',
            name='concern',
            field=models.ForeignKey(blank=True, db_column='concern', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Concern'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='concern',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ratelyyDatabase.Concern'),
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set(),
        ),
    ]
