# Generated by Django 3.2.6 on 2021-08-26 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12, null=True)),
                ('last_name', models.CharField(max_length=12, null=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('date_of_birth', models.DateField(max_length=10, null=True)),
                ('roll_number', models.CharField(max_length=10, null=True)),
                ('student_email', models.EmailField(max_length=254)),
                ('nationality', models.CharField(choices=[('Kenyan', 'Kenyan'), ('Ugandan', 'Ugandan'), ('Rwandeese', 'Rwandees'), ('South Sudaneese', 'South Sudaneese')], max_length=15)),
                ('student_id', models.CharField(max_length=18, null=True)),
                ('id_number', models.CharField(max_length=18, null=True)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6)),
                ('phone_number', models.CharField(max_length=16, null=True)),
                ('county', models.CharField(max_length=12, null=True)),
                ('profile', models.ImageField(null=True, upload_to='documents/')),
                ('medical_report', models.FileField(upload_to='')),
                ('date_of_enrollment', models.DateField(max_length=8, null=True)),
                ('language', models.CharField(choices=[('English', 'English'), ('Kiswahili', 'Kiswahili')], max_length=10)),
                ('serial_number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
