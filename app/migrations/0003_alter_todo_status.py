# Generated by Django 3.2.20 on 2023-08-09 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230807_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'Mark as Completed'), ('P', 'Pending')], default='P', max_length=2),
        ),
    ]
