# Generated by Django 3.2.6 on 2021-08-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='county',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_enrollment',
            field=models.DateField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='id_number',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=18, null=True),
        ),
    ]