from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id_brand', models.IntegerField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=45)),
                ('brand_logo', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'brands',
                'db_table': 'brands',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BrandsOld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fair', models.IntegerField()),
                ('eco', models.IntegerField()),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('concern_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'brands_old',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id_company', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=45)),
                ('company_logo', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name_plural': 'companies',
                'db_table': 'companies',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CompaniesOld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fair', models.IntegerField()),
                ('eco', models.IntegerField()),
                ('concern_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'companies_old',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Concerns',
            fields=[
                ('id_concern', models.IntegerField(primary_key=True, serialize=False)),
                ('concern_name', models.CharField(max_length=45)),
                ('concern_rating', models.CharField(choices=[('0', 'Neutral'), ('1', 'Ethical'), ('2', 'Unethical')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'concerns',
                'db_table': 'concerns',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConcernsOld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fair', models.IntegerField()),
                ('eco', models.IntegerField()),
            ],
            options={
                'db_table': 'concerns_old',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id_product', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=45)),
                ('product_ean', models.CharField(blank=True, max_length=45, null=True)),
                ('product_image', models.CharField(blank=True, max_length=45, null=True)),
                ('product_group', models.CharField(blank=True, max_length=200, null=True)),
                ('brands_id_brand', models.ForeignKey(db_column='brands_id_brand', on_delete=django.db.models.deletion.DO_NOTHING, to='ratelyyDatabase.Brands')),
            ],
            options={
                'verbose_name_plural': 'products',
                'db_table': 'products',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductsOld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ean', models.IntegerField()),
                ('fair', models.IntegerField()),
                ('eco', models.IntegerField()),
                ('concern_id', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'products_old',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='companies',
            name='concerns_id_concern',
            field=models.ForeignKey(db_column='concerns_id_concern', on_delete=django.db.models.deletion.DO_NOTHING, to='ratelyyDatabase.Concerns'),
        ),
        migrations.AlterUniqueTogether(
            name='products',
            unique_together={('id_product', 'brands_id_brand')},
        ),
        migrations.AlterUniqueTogether(
            name='companies',
            unique_together={('id_company', 'concerns_id_concern')},
        ),
    ]