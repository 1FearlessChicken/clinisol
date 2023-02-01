from django.db import models
from doctors.form import dept, blood_groups, gender


class general_details(models.Model):
    firstname = models.CharField('First Name', max_length=75)
    lastname = models.CharField('Last Name', max_length=75)
    other_names = models.CharField('Other Names', max_length=75)
    gender = models.CharField('Gender', choices= gender, max_length=75)
    age = models.DateField('Age')
    address = models.CharField('Home Address', max_length=250)
    phone_number = models.IntegerField('Phone Number')
    height = models.IntegerField('Height(cm)')
    weight = models.IntegerField('Weight(kg)')
    blood_group = models.CharField('Blood_Grop', choices= blood_groups, max_length=75)
    doctor_picture = models.ImageField('Passport', upload_to='static/images', null=True, blank=True, default='static/profile-icon.svg')
    staff_id = models.IntegerField('StaffNumber',)
    d_department = models.CharField('Department', choices= dept, max_length=75)
