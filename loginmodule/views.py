from django.shortcuts import render
from django.http import HttpResponseRedirect
from doctors.form import *
from .models import login_details
from doctors.models import*
from .form import login_form

from .form import NameForm


def signup_view(request):
    
    if request.method == "POST":
        form = general_details(request.POST,request.FILES)
        
        
        if form.is_valid():
            # f_name = form.cleaned_data['firstname']
            # l_name = form.cleaned_data['lastname']
            # o_names = form.cleaned_data['other_names']
            # gender = form.cleaned_data['gender']
            # address = form.cleaned_data['address']
            # age = form.cleaned_data['age']
            # p_number = form.cleaned_data['phone_number']
            # height = form.cleaned_data['height']
            # weight = form.cleaned_data['weight']
            # b_group = form.cleaned_data['blood_group']
            # department = form.cleaned_data['d_department']
            # s_id = form.cleaned_data['staff_id']
            #d_image = form.cleaned_data['inpFile']
            # if general_details.objects.filter(staff_id = s_id):
            #     varerr1="Doctor Already Exists"
            #     return render(request,'signup.html',{'form':form,'varerr':varerr1})
            # if "inpFile" in request.FILES:
            #     img = request.FILES['inpFile']
            # else:
            #     img = 'static/profile-icon.svg'
            # s = general_details(firstname = f_name, lastname = l_name, other_names = o_names, gender = gender, age = age, address = address,
            #                     phone_number = p_number, height = height, weight = weight, blood_group = b_group, doctor_picture = img,
            #                     staff_id = s_id, d_department = department)
            # s.save()
            # print(f_name)
            return HttpResponseRedirect('/test/')
            
        else:
            varerr1="Input All Fields"
            return render(request,'signup.html',{'form':form,'varerr':varerr1})
    else:
        form = general_details()
        return render(request,'signup.html',{'form':form})


def login_view(request):
    pass

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'test.html', {'form': form})