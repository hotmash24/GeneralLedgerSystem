# Generated by Django 4.2.2 on 2023-08-02 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcctSubsidiary',
            fields=[
                ('autonum', models.AutoField(primary_key=True, serialize=False)),
                ('primary_code', models.PositiveSmallIntegerField()),
                ('secondary_code', models.PositiveSmallIntegerField()),
                ('acct_code', models.PositiveSmallIntegerField()),
                ('subsidiary_code', models.PositiveSmallIntegerField()),
                ('subsidiary_acct_title', models.CharField(max_length=100)),
                ('subsidiary_acct_desc', models.CharField(blank=True, max_length=1000, null=True)),
                ('sl', models.CharField(blank=True, db_column='SL', max_length=1, null=True)),
                ('sl_type', models.CharField(blank=True, max_length=1, null=True)),
                ('calculation', models.PositiveSmallIntegerField()),
                ('alter_code', models.CharField(blank=True, max_length=50, null=True)),
                ('alter_name', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('sub_category', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'tbl_acct_subsidiary',
                'managed': False,
            },
        ),
    ]