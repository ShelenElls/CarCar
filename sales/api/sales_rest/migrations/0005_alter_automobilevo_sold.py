# Generated by Django 4.0.3 on 2022-06-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0004_remove_automobilevo_import_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobilevo',
            name='sold',
            field=models.BooleanField(),
        ),
    ]
