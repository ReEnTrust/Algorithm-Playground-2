# Generated by Django 2.0 on 2019-12-07 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_remove_applyjob_cv'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApplyJob',
            new_name='JobApply',
        ),
    ]