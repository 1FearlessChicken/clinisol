from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from patients.form import *
from patients.models import Patients


def details_views(request):
    
    if request.method == "POST":
        form = general_details(request.POST, request.FILES)

        if form.is_valid():
            f_name = form.cleaned_data['firstname']
            l_name = form.cleaned_data['lastname']
            o_names = form.cleaned_data['other_names']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            p_number = form.cleaned_data['phone_number']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            blood_group = form.cleaned_data['blood_group']
            admission_number = form.cleaned_data['add_number']
            
            #s_image = form.cleaned_data['inpFile']
            if Patients.objects.filter(add_number = admission_number):
                varerr1="Patient Already Exists"
                #return render(request,'index.html',{'form':form,'varerr':varerr1})
            #if "inpFile" in request.FILES:
            #    img = request.FILES['inpFile']
            #else:
            #    img = 'patient_picture/user.png'
            s = Patients(firstname = f_name, lastname = l_name, other_names = o_names , gender = gender, age = age, address = address, phone_number = p_number, height = height, weight = weight, blood_group = blood_group, add_number = admission_number)
            s.save()
            return HttpResponseRedirect('/patients')
            
        else:
            varerr1="Input All Fields"
            return render(request,'index.html', {'form':form,'varerr':varerr1})

    else:
        form = general_details()
        return render(request,'index.html',{'form':form})
 