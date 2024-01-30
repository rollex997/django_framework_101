# Generated by Django 4.2.8 on 2024-01-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0004_marks_settings_marks_failed_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks_settings',
            name='passing_marks_per_subject',
            field=models.FloatField(default=40),
        ),
        migrations.AlterField(
            model_name='marks_settings',
            name='passing_percentage',
            field=models.FloatField(default=40),
        ),
    ]