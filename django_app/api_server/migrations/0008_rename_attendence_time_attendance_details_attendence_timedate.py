# Generated by Django 4.1.2 on 2023-05-01 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0007_rename_name_student_details_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance_details',
            old_name='attendence_time',
            new_name='attendence_timedate',
        ),
    ]
