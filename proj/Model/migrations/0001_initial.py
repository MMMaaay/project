# Generated by Django 3.2.6 on 2021-08-18 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('AliasName', models.CharField(max_length=255)),
                ('AccoutID', models.CharField(max_length=20)),
            ],
        ),
    ]
