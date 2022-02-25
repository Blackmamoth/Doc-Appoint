from django.shortcuts import redirect, render
from .forms import RegistrationForm, AppointmentForm
from django.contrib import messages
from .models import Appointment, Doctor
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from datetime import datetime, timedelta



def home(request):
    if request.user.is_authenticated:
        appointments = request.user.appointment_set.all()
    else:
        appointments = None
    return render(request, 'appointments/home.html', {'appointments': appointments})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created you can now login!!!')
            return redirect('login')
    return render(request, 'appointments/register.html', {'form': form})

@login_required(login_url='login')
def appoint(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            doctor = form.cleaned_data.get('doctor')
            date = form.cleaned_data.get('date')
            checkup_for = form.cleaned_data.get('checkup_for')
            today = datetime.today()
            if not datetime.strptime(date, "%Y-%m-%d") > today:
                messages.info(request ,f'{doctor} is not avaiable until tommorow please set the date likewise') 
            else:
                appointment = Appointment(patient=request.user, doctor=doctor, date=date, checkup_for=checkup_for)
                appointment.save()
                messages.success(request,"Appointment added, don't miss it!!!")
                return redirect('home')
    return render(request, 'appointments/appoint.html', {'form': form})


@login_required(login_url='login')
def delete_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    if appointment.patient.username != request.user.username:
        raise PermissionDenied
    if request.method == 'POST':
        appointment.delete()
        return redirect('home')
    return render(request, 'appointments/delete_appointment.html', {'appointment': appointment})

@login_required(login_url='login')
def postpone(request, id):
    appointment = Appointment.objects.get(id=id)
    form = AppointmentForm(instance=appointment)
    if appointment.patient.username != request.user.username:
        raise PermissionDenied
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            day_after_tommorow = datetime.today() + timedelta(1)
            if not datetime.strptime(date, "%Y-%m-%d") >= day_after_tommorow:
                messages.info(request, 'You can now only reschedule the meeting to day after tommorow')
            else:
                form.save()
                messages.info(request,'Reschedule accepted!!!')
                return redirect('home')
    return render(request, 'appointments/postpone.html', {'form': form})

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/doctors.html', {'doctors': doctors})