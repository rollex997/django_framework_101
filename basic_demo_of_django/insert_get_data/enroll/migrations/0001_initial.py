# Generated by Django 4.2.8 on 2024-01-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('SID', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('mobile', models.BigIntegerField()),
                ('city', models.CharField(max_length=70)),
                ('roll_number', models.IntegerField()),
            ],
        ),
    ]
