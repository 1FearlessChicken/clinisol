from argparse import Action
import email
from django import forms

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

class general_details(forms.Form):
    firstname = forms.CharField(label='FirstName', widget=forms.TextInput({ "placeholder": "First Name"}), min_length=2, max_length=15)
    lastname = forms.CharField(label='LastName', widget=forms.TextInput({ "placeholder": "Last Name"}), min_length=2, max_length=15)
    other_names = forms.CharField(label='OtherNames', widget=forms.TextInput({ "placeholder": "Other Names"}), min_length=2, max_length=15)
    gender = forms.ChoiceField(label='gender', choices= gender)
    age = forms.IntegerField(label='Age', widget=forms.DateInput({"placeholder": "Date of Birthe"}))
    address = forms.CharField(label='Address', widget=forms.TextInput({"placeholder": "Address"}), min_length=8, max_length=100)
    phone_number = forms.IntegerField(label='PhoneNumber', widget=forms.TextInput({"placeholder": "Phone Number"}),)
    height = forms.CharField(label='height', widget=forms.NumberInput({"placeholder": "Height in meters"}))
    weight = forms.CharField(label='weight', widget=forms.NumberInput({"placeholder": "weight in kgs"}))
    blood_group = forms.ChoiceField(label='bloodgroup', choices= blood_groups)
    inpFile = forms.ImageField(label='patient picture',required=False)

    
    def __init__(self, *args):
        super(general_details, self).__init__(*args)
        self.fields['inpFile'].widget.attrs['class'] = 'file-input'
        self.fields['admitted_session'].widget.attrs['class'] = 'form-control'