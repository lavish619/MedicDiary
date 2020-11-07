# Generated by Django 3.0.7 on 2020-11-07 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDocConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('access_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Gender', models.CharField(max_length=30)),
                ('Specialisation', models.CharField(max_length=30)),
                ('phone', models.CharField(help_text='10 digit Mobile Number', max_length=40)),
                ('City', models.CharField(max_length=30)),
                ('Registration_Number', models.CharField(max_length=40)),
                ('Registration_Council', models.CharField(max_length=100)),
                ('Registration_year', models.IntegerField()),
                ('Degree', models.CharField(max_length=100)),
                ('College', models.CharField(max_length=100)),
                ('Year_of_completion', models.IntegerField()),
                ('Profile_pic', models.ImageField(default='doctors_profile_pictures/defaultprofilepic.jpg', upload_to='doctors_profile_pictures')),
                ('Medical_registration_proof', models.FileField(blank=True, upload_to='DoctorRegProofs')),
                ('Current_place_of_work', models.CharField(max_length=30)),
                ('Aadhar_Number', models.IntegerField(help_text='12 digit unique Aadhar Number')),
                ('usertype', models.IntegerField(default=2)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
