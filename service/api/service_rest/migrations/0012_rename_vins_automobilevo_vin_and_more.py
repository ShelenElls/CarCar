# Generated by Django 4.0.3 on 2022-06-21 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0011_alter_status_options_automobilevo_color_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='automobilevo',
            old_name='vins',
            new_name='vin',
        ),
        migrations.AddField(
            model_name='automobilevo',
            name='manufacturer',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
