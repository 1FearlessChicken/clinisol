# Generated by Django 4.1 on 2023-02-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_alter_general_details_staff_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='d_general_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=75, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=75, verbose_name='Last Name')),
                ('other_names', models.CharField(max_length=75, verbose_name='Other Names')),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=75, verbose_name='Gender')),
                ('age', models.DateField(verbose_name='Age')),
                ('address', models.CharField(max_length=250, verbose_name='Home Address')),
                ('phone_number', models.IntegerField(verbose_name='Phone Number')),
                ('height', models.IntegerField(verbose_name='Height(cm)')),
                ('weight', models.IntegerField(verbose_name='Weight(kg)')),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('O +', 'A+'), ('B+', 'A+'), ('AB+', 'A+'), ('A-', 'A+'), ('O-', 'A+'), ('B-', 'A+'), ('AB-', 'AB-')], max_length=75, verbose_name='Blood_Grop')),
                ('doctor_picture', models.ImageField(blank=True, default='static/profile-icon.svg', null=True, upload_to='static/images', verbose_name='Passport')),
                ('staff_id', models.IntegerField(verbose_name='StaffNumber')),
                ('d_department', models.CharField(choices=[('Cardiology', 'Cardiology'), ('Neurosurgery', 'Neurosurgery'), ('ENT', 'ENT'), ('General Surgery', 'General Surgery'), ('Radiology', 'Radiology'), ('Intensive Care', 'Intensive Care'), ('Orthopedic', 'Orthopedic'), ('Gynaecology', 'Gynaecology'), ('Pharmacy', 'Pharmacy'), ('Haematology', 'Haematology'), ('Paediatric', 'Paediatric'), ('Obstetrics', 'Obstetrics')], max_length=75, verbose_name='Department')),
            ],
        ),
        migrations.DeleteModel(
            name='general_details',
        ),
    ]
