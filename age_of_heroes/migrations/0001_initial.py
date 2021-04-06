# Generated by Django 3.1.7 on 2021-04-05 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0008_auto_20210405_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_sugar_level', models.FloatField()),
                ('blood_pressure', models.FloatField()),
                ('body_temperature', models.FloatField()),
                ('weight', models.FloatField()),
                ('xray', models.BooleanField()),
                ('mri_scan', models.BooleanField()),
                ('blood_sodium_level', models.FloatField()),
                ('other_diagonosis', models.TextField()),
                ('previous_medical_conditions', models.TextField()),
                ('current_medical_condition', models.TextField()),
                ('cause', models.CharField(max_length=20)),
                ('height', models.FloatField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_report_patient', to='accounts.patientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('expected_time', models.TimeField()),
                ('token_number', models.CharField(max_length=20)),
                ('token_id', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='accounts.doctorprofile')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='accounts.patientprofile')),
            ],
        ),
    ]
