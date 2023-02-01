from django.db import models

# Create your models here.
gender=(
    ('male','MALE'),
    ('female','FEMALE'),
    )

blood_groups=(
    ('A+','A+'),
    ('O +','A+'),
    ('B+','A+'),
    ('AB+','A+'),
    ('A-','A+'),
    ('O-','A+'),
    ('B-','A+'),
    ('AB-','AB-'),
)

class Patients(models.Model):
    firstname = models.CharField('First Name', max_length=75)
    lastname = models.CharField('Last Name', max_length=75)
    other_names = models.CharField('Other Names', max_length=75)
    gender = models.CharField('Gender', choices= gender, max_length=75)
    age = models.IntegerField('Age')
    address = models.CharField('Home Address', max_length=120)
    phone_number = models.IntegerField('Phone Number')
    height = models.IntegerField('Height(cm)')
    weight = models.IntegerField('Weight(kg)')
    blood_group = models.CharField('Blood_Grop', choices= blood_groups, max_length=75)
    patient_picture = models.ImageField('Passport', upload_to='patient_picture', null=True, blank=True, default='patient_picture/user.png')
    add_number = models.IntegerField('Admission Number')