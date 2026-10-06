"""
URL configuration for Hospital_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),  
    path('', base, name='base'),
    path('patient_add/',PatientView,name='patient_add'),
    path('viewpatient/',viewpatients,name='viewpatient'),
    path('editpatient/<str:aadhar>',modifypatient,name='editpatient'),
    path('deletepatient/<str:aadhar>',deletepatient,name='deletepatient'),
    path('doctor_add/',AddDoctordetail,name='doctor_add'),
    path('viewdoctor/',viewdoctor,name='viewdoctor'),
    path('edidoctor/<str:id>',modifdoctor,name='editdoctor'),
    path('deletedoctor/<str:id>',deletdoctor,name='deletedoctor'),
    path('appointment_add/', AddAppointment, name='appointment_add'),
    path('view_appointment/', ViewAppointments, name='view_appointment'),
    path('edit_appointment/<int:appointment_id>/', ModifyAppointment, name='modify_appointment'),
    path('delete_appointment/<int:appointment_id>/', DeleteAppointment, name='delete_appointment'),
  
    path('addbill/<int:appointment_id>/', AddBill, name='add_bill'),
    path('select_appointment/', SelectAppointmentForBill, name='select_appointment_for_bill'),
    path('view_bills/', ViewBills, name='view_bills'),
    path('editbill/<int:bill_id>/', EditBill, name='edit_bill'),
    path('deletebill/<int:bill_id>/', DeleteBill, name='delete_bill'),


]
