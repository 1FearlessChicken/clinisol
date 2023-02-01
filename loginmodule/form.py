from django import forms


class login_form(forms.Form):
    staff_identification_no = forms.CharField(label='StaffID',)
    password = forms.CharField(label='Password', widget=forms.TextInput({ "placeholder": "Password"}))


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)