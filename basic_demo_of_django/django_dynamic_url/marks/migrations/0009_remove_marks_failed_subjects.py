# Generated by Django 4.2.8 on 2024-01-29 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0008_remove_marks_total_marks_per_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='failed_subjects',
        ),
    ]
