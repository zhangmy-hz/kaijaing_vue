# Generated by Django 2.1.15 on 2020-11-03 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaijaing', '0091_warehous_del_out_warehousing_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='draw_time',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
