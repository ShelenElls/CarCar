# Generated by Django 4.0.3 on 2022-06-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0005_alter_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
