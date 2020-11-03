# Generated by Django 2.1.15 on 2020-10-21 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaijaing', '0090_auto_20201021_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehous_Del_Out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_key', models.CharField(default='', max_length=20)),
                ('item_code', models.CharField(max_length=20)),
                ('item_name', models.CharField(max_length=200)),
                ('format', models.CharField(max_length=20)),
                ('unit', models.CharField(default='', max_length=20)),
                ('num', models.IntegerField()),
                ('note', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(default='未审核', max_length=20)),
                ('create_user', models.CharField(max_length=40, null=True)),
                ('date', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehousing_Out',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=40, null=True)),
                ('note', models.CharField(max_length=200, null=True)),
                ('create_time', models.CharField(max_length=40, null=True)),
                ('examine', models.CharField(max_length=40, null=True)),
                ('examine_time', models.CharField(max_length=40, null=True)),
                ('create_user', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]
