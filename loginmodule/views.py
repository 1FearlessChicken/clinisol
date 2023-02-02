from django.shortcuts import render
from django.http import HttpResponseRedirect
from doctors.form import *
from .models import d_login_details
from doctors.models import*
from .form import login_form


def d_signup_view(request):
    if request.method == 'POST':
        form = general_details_d(request.POST, request.FILES)
        
        if form.is_valid():
            f_name = form.cleaned_data['firstname']
            l_name = form.cleaned_data['lastname']
            o_names = form.cleaned_data['other_names']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            age = form.cleaned_data['age']
            p_number = form.cleaned_data['phone_number']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            b_group = form.cleaned_data['blood_group']
            department = form.cleaned_data['d_department']
            s_id = form.cleaned_data['staff_id']
            #d_image = form.cleaned_data['inpFile']
            if d_general_details.objects.filter(staff_id = s_id):
                varerr1="Doctor Already Exists"
                return render(request,'signup.html',{'form':form,'varerr':varerr1})
            if "inpFile" in request.FILES:
                img = request.FILES['inpFile']
            else:
                img = 'static/profile-icon.svg'
            s = d_general_details(firstname = f_name, lastname = l_name, other_names = o_names, gender = gender, age = age, address = address,
                                phone_number = p_number, height = height, weight = weight, blood_group = b_group, doctor_picture = img,
                                staff_id = s_id, d_department = department)
            s.save()
            print(s_id)
            return HttpResponseRedirect('/loginmodule/signup')
        else:
            varerr1="Input all fields"
            return render(request,'signup.html', {'form':form,'varerr':varerr1})
    else:
        form = general_details_d
        return render(request,'signup.html', {'form':form})
        

# def login_view(request):
    
#     if request.method == 'POST':
#         form = login_form(request.POST)
        
#         if form.is_valid():
#             staffid_no = form.cleaned_data['staff_identification_no']
#             p_word = form.cleaned_data['password']
            
#             if d_general_details.objects.filter(staff_id = staffid_no) and d_general_details.objects.filter(password = p_word):
#                 print('Access Granted')
#                 return HttpResponseRedirect('/loginmodule/signup/')
#             else:
#                 varerr='Wrong Credentials, Try Again'
#                 return render(request,'login.html',{'form':form,'varerr':varerr})
#         else:
#             return render(request,'login.html',{'form':form})
        
#     else:
#         form = login_form()
#         return render(request,'login.html',{'form':form})


# def login_view(request):
    
#     if request.method == "POST":
#         form = login_form(request.POST)

#         if form.is_valid():
#             registrationNo = form.cleaned_data['registrationNo']
#             print(registrationNo)
#             if Students.objects.filter(admissionno = registrationNo):
#                 d=Students.objects.get(admissionno = registrationNo)
#                 return HttpResponseRedirect('students/disclaimer/%s/'%d.id)
#             else:
#                 varerr="invalid user"
#                 return render(request,'students/login.html',{'form':form,'varerr':varerr})
#         else:
#             return render(request,'students/login.html',{'form':form})

#     else:
#         form = login_form()
#         return render(request,'students/login.html',{'form':form})