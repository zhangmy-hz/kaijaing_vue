# Generated by Django 2.1.15 on 2020-08-02 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaijaing', '0039_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('size_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('size_name', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
