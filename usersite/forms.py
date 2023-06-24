from django import forms
from django.forms import ModelForm
from . models import admission_details,personal_details
from django.contrib.auth.models import User

class admissionForm(ModelForm):
     class Meta:
        model = admission_details
        fields = ['year_admission','category_admission','hsc_marks','cet_marks','jee_marks','diploma_marks']


class personalDetailsForm(ModelForm):
        class Meta:
                model = personal_details
                widgets ={
                        'birth_date':forms.TextInput(attrs={'placeholder':'YYYY/MM/DD'})
                 }
                fields = ['birth_place','mother_tongue','religion','address','phone_number','email','blood_group','guardian_name','birth_date','stud_sign_image','disease']



# class familyDetailsForm(ModelForm):
#         class Meta:
#                 model = fami



