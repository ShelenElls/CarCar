# Generated by Django 4.0.3 on 2022-06-20 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0006_appointment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='vins',
        ),
        migrations.AddField(
            model_name='appointment',
            name='vinnew',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='technician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appointmenttech', to='service_rest.technician'),
        ),
        migrations.CreateModel(
            name='AptHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vins', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='apthistorys', to='service_rest.automobilevo')),
            ],
        ),
    ]
