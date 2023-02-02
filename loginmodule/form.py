from django import forms


class login_form(forms.Form):
    staff_identification_no = forms.CharField(label='StaffID',)
    password = forms.CharField(label='Password', widget=forms.TextInput({ "placeholder": "Password"}))
