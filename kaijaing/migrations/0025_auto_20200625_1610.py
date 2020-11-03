# Generated by Django 2.1.15 on 2020-06-25 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaijaing', '0024_auto_20200620_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_del',
            name='amount',
            field=models.FloatField(default=0, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order_del',
            name='order_level',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order_del',
            name='order_type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
