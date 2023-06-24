from django.db import models
from django.contrib.auth.models import User



class personal_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
    middle_name=models.CharField(max_length=30)
    birth_place=models.CharField(max_length=30)
    birth_date=models.DateField()
    mother_tongue=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=30)
    guardian_name=models.CharField(max_length=30,default="NULL")
    religion=models.CharField(max_length=30)
    blood_group=models.CharField(max_length=30)
    disease=models.CharField(max_length=30,default="None")
    address=models.CharField(max_length=100,default="NULL")
    stud_image=models.ImageField(upload_to ="images/")
    stud_sign_image=models.ImageField(upload_to ="images/")
    email=models.CharField(max_length=30,default="NULL")
    family_income=models.IntegerField(default=10000)




class current_semester(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)    
    user =models.ForeignKey(User,on_delete=models.CASCADE)    
    current_year=models.IntegerField(default=2020)
    # CURRENT_SEM_CHOICES =[
    #     ('SEM 1','SEM 1'),
    #     ('SEM 2','SEM 2'),
    #     ('SEM 3','SEM 3'),
    #     ('SEM 4','SEM 4'),
    #     ('SEM 5','SEM 5'),
    #     ('SEM 6','SEM 6'),
    #     ('SEM 7','SEM 7'),
    #     ('SEM 8','SEM 8'),
    # ]
    current_sem=models.CharField(max_length=50)



class semester_sub_ia(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    current_semester=models.ForeignKey('current_semester',on_delete=models.CASCADE)
    sub_1=models.CharField(max_length=30)
    sub_2=models.CharField(max_length=30)
    sub_3=models.CharField(max_length=30)
    sub_4=models.CharField(max_length=30)
    sub_5=models.CharField(max_length=30)
    sub_6=models.CharField(max_length=30)


class attendance(models.Model):
    current_sem=models.ForeignKey('current_semester',on_delete=models.CASCADE)
    # email=models.ForeignKey(user,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    default_list_num=models.IntegerField()
    is_defaulter=models.BooleanField()



    # family models

class family_relation(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      relation_type=models.CharField(max_length=30)



class family_info(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    femail=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    contact_num=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    occupation=models.CharField(max_length=30)
    relation_type=models.ForeignKey('family_relation',on_delete=models.CASCADE)



class admission_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    jee_marks=models.DecimalField(max_length=50,max_digits=5,decimal_places=2)
    hsc_marks=models.DecimalField(max_length=50,max_digits=5,decimal_places=2)
    cet_marks=models.DecimalField(max_length=50,max_digits=5,decimal_places=2)
    diploma_marks=models.DecimalField(max_length=50,max_digits=5,decimal_places=2)
    year_admission=models.IntegerField(default=0000)
    category_admission=models.CharField(max_length=50)

    


    



