from django.db import models

# Create your models here.
class Patient(models.Model):
    AaadharNo=models.CharField(max_length=12,primary_key=True)
    Name=models.CharField(max_length=50)
    Mob=models.CharField(max_length=10)

    class Meta:
        db_table='patient'

    def __str__(self):
        return f'Name: {self.Name}, Aadhar No: {self.AaadharNo}, Mobile: {self.Mob}'
    

class Doctor(models.Model):
    DoctorId=models.CharField(max_length=3,primary_key=True)
    DoctorName=models.CharField(max_length=50)
    DoctorDepartement=models.CharField(max_length=13)

    class Meta:
        db_table='doctor'

    def __str__(self):
        return f'Doctor Id:{self.DoctorId}, Doctor Name : {self.DoctorName}, Doctor Department: {self.DoctorDepartement}'    


class Appointment(models.Model):
    AppointmentId = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    AppointmentDate = models.DateField()
    AppointmentTime = models.TimeField()
    Description = models.TextField(blank=True, null=True)  

    class Meta:
        db_table = 'appointment'

    def __str__(self):
        return f'Appointment {self.AppointmentId} - Patient: {self.Patient.Name}, Doctor: {self.Doctor.DoctorName}, Date: {self.AppointmentDate}'

class Bill(models.Model):
    BillId = models.AutoField(primary_key=True)
    Appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    PAYMENT_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]
    PaymentStatus = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='Unpaid')

    class Meta:
        db_table = 'bill'

    def __str__(self):
        return f'Bill {self.BillId} - Appointment {self.Appointment.AppointmentId} - Status: {self.PaymentStatus}'

    