from django.shortcuts import render,redirect,get_object_or_404
from app1.models import Patient,Doctor,Appointment,Bill
from django.utils.dateparse import parse_date, parse_time
# Create your views here.

def base(request):
    return render(request,'base.html' ,context={})

def home(request):
     return render(request, 'home.html',context={})


def PatientView(request):
    msg = ''
    if request.method == 'POST':
        aadhar=request.POST.get('Aadhar')
        name=request.POST.get('Name')
        num=request.POST.get('Num')

        Patient.objects.create(AaadharNo=aadhar,Name=name,Mob=num)
        msg="add patient sucessfully"
        return redirect('patient_add')
    
    return render(request, 'addpatient.html', {'msg': msg})

def viewpatients(request):
    pat = Patient.objects.all()
    return render(request, 'view_patient.html', context={'pat': pat})


def modifypatient(request,aadhar):
    # if request.method=="POST":
    #     name=request.POST.get(Name):
    patient=get_object_or_404(Patient, AaadharNo=aadhar)
    if request.method=="POST":
            name=request.POST.get('Name')
            mobile=request.POST.get('Num')

            patient.Name=name
            patient.Mob=mobile
            patient.save()
            return redirect('viewpatient')

    return render(request, 'edit_patient.html',context={'patient':patient})

def deletepatient(request,aadhar):
    patient = get_object_or_404(Patient, AaadharNo=aadhar)
    patient.delete()
    return redirect('viewpatient')
def AddDoctordetail(request):
    msg=''
    if request.method =='POST':
         did=request.POST.get('DoctorId')
         dname=request.POST.get('DoctorName')
         dpartement=request.POST.get('DoctorDepartement')

         Doctor.objects.create(DoctorId=did,DoctorName=dname,DoctorDepartement=dpartement)
         msg='Add sucessfully'
         return redirect('doctor_add')
    return render(request,'adddoctor.html',{'msg':msg})   
def viewdoctor(request):
    doc = Doctor.objects.all()
    return render(request, 'view_doctor.html', context={'doc': doc}) 
def modifdoctor(request,id):
    doctor=get_object_or_404(Doctor, DoctorId=id)
    if request.method=="POST":
            name=request.POST.get('Name')
            departement=request.POST.get('DEP')

            doctor.DoctorName=name
            doctor.DoctorDepartement=departement
            doctor.save()
            return redirect('viewdoctor')

    return render(request, 'edit_doctor.html',context={'doctor':doctor})
def deletdoctor(request,id):
    doctor = get_object_or_404(Doctor, DoctorId=id)
    doctor.delete()
    return redirect('viewdoctor')





# Add Appointment
def AddAppointment(request):
    msg = ''
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        patient_id = request.POST.get('PatientId')
        doctor_id = request.POST.get('DoctorId')
        date = request.POST.get('AppointmentDate')
        time = request.POST.get('AppointmentTime')
        description = request.POST.get('Description', '')

        patient = get_object_or_404(Patient, AaadharNo=patient_id)
        doctor = get_object_or_404(Doctor, DoctorId=doctor_id)

        Appointment.objects.create(
            Patient=patient,
            Doctor=doctor,
            AppointmentDate=parse_date(date),
            AppointmentTime=parse_time(time),
            Description=description
        )
        msg = "Appointment added successfully"
        return redirect('appointment_add')

    context = {'msg': msg, 'patients': patients, 'doctors': doctors}
    return render(request, 'addappointment.html', context)


def ViewAppointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'view_appointment.html', {'appointments': appointments})


def ModifyAppointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, AppointmentId=appointment_id)
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        patient_id = request.POST.get('PatientId')
        doctor_id = request.POST.get('DoctorId')
        date = request.POST.get('AppointmentDate')
        time = request.POST.get('AppointmentTime')
        description = request.POST.get('Description', '')

        appointment.Patient = get_object_or_404(Patient, AaadharNo=patient_id)
        appointment.Doctor = get_object_or_404(Doctor, DoctorId=doctor_id)
        appointment.AppointmentDate = parse_date(date)
        appointment.AppointmentTime = parse_time(time)
        appointment.Description = description
        appointment.save()

        return redirect('view_appointment')

    context = {'appointment': appointment, 'patients': patients, 'doctors': doctors}
    return render(request, 'edit_appointment.html', context)


def DeleteAppointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, AppointmentId=appointment_id)
    appointment.delete()
    return redirect('view_appointment')

def SelectAppointmentForBill(request):
    appointments = Appointment.objects.all()
    return render(request, 'select_appointment.html', {'appointments': appointments})

def AddBill(request, appointment_id):
    appointment = get_object_or_404(Appointment, AppointmentId=appointment_id)
    msg = ''

    if request.method == 'POST':
        amount = request.POST.get('Amount')
        payment_status = request.POST.get('PaymentStatus', 'Unpaid')

       
        if hasattr(appointment, 'bill'):
            msg = 'Bill already exists for this appointment.'
        else:
            Bill.objects.create(
                Appointment=appointment,
                Amount=amount,
                PaymentStatus=payment_status
            )
            msg = 'Bill generated successfully.'
            return redirect('view_bills')

    context = {'appointment': appointment, 'msg': msg}
    return render(request, 'addbill.html', context)



def ViewBills(request):
    bills = Bill.objects.all()
    return render(request, 'view_bills.html', {'bills': bills})



def EditBill(request, bill_id):
    bill = get_object_or_404(Bill, BillId=bill_id)

    if request.method == 'POST':
        bill.Amount = request.POST.get('Amount')
        bill.PaymentStatus = request.POST.get('PaymentStatus')
        bill.save()
        return redirect('view_bills')

    context = {'bill': bill, 'payment_choices': Bill.PAYMENT_CHOICES}
    return render(request, 'editbill.html', context)


def DeleteBill(request, bill_id):
    bill = get_object_or_404(Bill, BillId=bill_id)
    bill.delete()
    return redirect('view_bills')
