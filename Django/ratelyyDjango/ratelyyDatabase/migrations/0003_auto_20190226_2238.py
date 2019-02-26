# Generated by Django 2.1.7 on 2019-02-26 21:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0002_auto_20190226_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='concerns',
            name='concern_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='concerns',
            name='concern_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand_logo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Brand Logo'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand_name',
            field=models.CharField(max_length=45, verbose_name='Brand Name'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='companies',
            field=models.ManyToManyField(to='ratelyyDatabase.Companies', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='company_logo',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Company Logo'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='company_name',
            field=models.CharField(max_length=45, unique=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='concerns_id_concern',
            field=models.ForeignKey(db_column='concerns_id_concern', on_delete=django.db.models.deletion.DO_NOTHING, to='ratelyyDatabase.Concerns', verbose_name='Concern'),
        ),
        migrations.AlterField(
            model_name='concerns',
            name='concern_name',
            field=models.CharField(max_length=45, unique=True, verbose_name='Concern Name'),
        ),
        migrations.AlterField(
            model_name='concerns',
            name='concern_rating',
            field=models.CharField(choices=[('0', 'Neutral'), ('1', 'Ethical'), ('2', 'Unethical')], default=0, max_length=2, verbose_name='Concern Rating'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]