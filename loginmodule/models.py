from django.db import models
from doctors.models import *
from nurses.models import *
    
    
class login_details(models.Model):
    staff_id_no = models.ForeignKey("general_details", on_delete=models.CASCADE)
    password = models.CharField('Password', max_length=15)
    
    def staff_id_no(self):
        return self.staff_id_no.staff_id
    
    