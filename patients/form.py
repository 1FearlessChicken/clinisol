from argparse import Action
from django import forms
from random import choices
from secrets import choice
from patients.models import Patients

gender=(
    ('male','MALE'),
    ('female','FEMALE'),
)

genotype=(
    ('AA', 'AA'),
    ('AS', 'AS'),
    ('AC', 'AC'),
    ('SS', 'SS'),
    ('SC', 'SC')
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

class general_details(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField(label='LastName', widget=forms.TextInput({ "placeholder": "Last Name"}))
    other_names = forms.CharField(label='OtherNames', widget=forms.TextInput({ "placeholder": "Other Names"}))
    gender = forms.ChoiceField(label='Gender', choices= gender)
    age = forms.IntegerField(label='Age', widget=forms.DateInput({"placeholder": "Date of Birthe"}))
    address = forms.CharField(label='Address', widget=forms.TextInput({"placeholder": "Address"}))
    phone_number = forms.IntegerField(label='PhoneNumber', widget=forms.NumberInput({"placeholder": "Phone Number"}))
    height = forms.CharField(label='height', widget=forms.NumberInput({"placeholder": "Height in meters"}))
    weight = forms.CharField(label='weight', widget=forms.NumberInput({"placeholder": "weight in kgs"}))
    blood_group = forms.ChoiceField(label='bloodgroup', choices= blood_groups)
    genotype = forms.ChoiceField(label='genotype', choices= genotype)
    admission_number = forms.IntegerField(label='AdmissionNumber', widget=forms.NumberInput({"placeholder": "Patient's Admission Number"}))
    occupation = forms.CharField(label='occupation', widget=forms.TextInput({"placeholder": "Occupation"}))
    #inpFile = forms.ImageField(label='patient picture',required=False)


    
    #def __init__(self, *args):
    #    super(general_details, self).__init__(*args)
    #    self.fields['inpFile'].widget.attrs['class'] = 'file-input'
        

class clinical_examination_details:
    date = forms.DateField(label='Todays Date',)
    bp = forms.CharField(label='bp')
    
    

class diagnosis:
    pass

class treatment:
    pass

class follow_up:
    pass

class investigation:
    pass

class bill:
    pass