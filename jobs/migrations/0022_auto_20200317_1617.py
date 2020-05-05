# Generated by Django 3.0.4 on 2020-03-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_auto_20200317_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='education',
            field=models.IntegerField(choices=[(1, 'Undergraduate'), (2, 'Bachelor Degree'), (3, 'Master Degree'), (4, 'PhD')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='experience',
            field=models.IntegerField(choices=[(0, 'Entry Level'), (1, 'New 0 to 2 years'), (2, 'Moderate 3 to 5 years'), (3, 'Experienced 6 to 8 years'), (4, 'Very experienced 9 to 10 years'), (5, 'Super experienced 11 years and above')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='location',
            field=models.IntegerField(choices=[(0, '400 to 499 miles away'), (1, '300 to 399 miles away'), (2, '200 to 299 miles away'), (3, '100 to 199 miles away'), (4, '5 to 99 miles away')], default='', max_length=100),
        ),
    ]