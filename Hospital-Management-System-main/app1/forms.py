# from django import forms
# from django.core.validators import*
# from app1.models import Patient

# class Patientform(forms.ModelForm):
#     AaadharNo=forms.CharField(
#         label='Aadhar Number ',
#         widget=forms.TextInput(attrs={
#             'class':'form-control w-50 mt-1 border border-2 bg-warning text-dark fw-bold',
#             'placeholder':'Enter 12 digit Number text-white'
#         }),
#         validators=[
#             RegexValidator(r'^\d{12}$',message='Aadhar must be 12 digit')
#          ]
#     )
#     Name=forms.CharField(
#         label='Full Name',
#         widget=forms.TextInput(attrs={
#             'class':'form-control w-50 mt-1 bg-warning text-dark fw-bold',
#             'placeholder':'Enter the Name'
#         }),
#         validators=[
#             RegexValidator(r'^[A-Za-z\s]+$', message='Name must contain only letters and spaces')
    
#         ]

#     )
#     Mob=forms.CharField(
#         label='Mobile Number',
#         widget=forms.TextInput(attrs={
#             'class':'form-control w-50 mt-1 bg-warning text-dark fw-bold',
#             'placeholder':'Enter 10 digit Mobile Number'
#         }),
#         validators=[
#             RegexValidator(r'^[6-9]\d{9}$',message='Mobile number Must 10 digit ')
#         ]
#     )
#     class Meta:
#         model=Patient
#         fields='__all__'