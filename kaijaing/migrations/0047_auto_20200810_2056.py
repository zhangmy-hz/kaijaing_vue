# Generated by Django 2.1.15 on 2020-08-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaijaing', '0046_auto_20200810_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quanxian',
            name='sort',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
