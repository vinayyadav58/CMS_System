# from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from .forms import AddDoctorForm,DoctorVisitsForm
from .models import Doctor,Appointment,Deal
from django.contrib import messages
from django.views.generic import ListView,CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ScheduleAppointmentForm,visitDoctorVisitsForm
from .forms import DealForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum,Count




# Create your views here.


@login_required(login_url='/')
def add_doctor(request):
    if request.method == 'POST':
        form = AddDoctorForm(request.POST,request.FILES)
        if form.is_valid():
            doctor_name = form.cleaned_data['doctor_name']
            specialisation = form.cleaned_data['specialisation']
            contact_number= form.cleaned_data['contact_number']
            location = form.cleaned_data['location']
            entered_by = form.cleaned_data['entered_by']
            # form.save()
            doctor = Doctor(
                doctor_name=doctor_name,
                specialisation=specialisation,
                contact_number=contact_number,
                location=location,
                entered_by=entered_by
                )
            doctor.save()

            messages.success(request,"New doctor added succesfully ")
            return redirect('test')
    else:
        form = AddDoctorForm()
    
    context = {'form': form}
    return render(request, 'doctor/add_doctor.html', context)
    



# def sc_doctor(request):
#         return render(request, 'doctor/sc_doctor.html')

    
from django.shortcuts import render, redirect

@login_required(login_url='/')
def schedule_appointment(request):
    if request.method == 'POST':
        form = ScheduleAppointmentForm(request.POST)
        if form.is_valid():
            doctor = form.cleaned_data['doctor']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            entered_by = form.cleaned_data['entered_by']

            appointment = Appointment(
                doctor=doctor,
                date=date,
                time=time,
                entered_by=entered_by

            )
            appointment.save()

           
            messages.success(request," Appointment Schedule Succesfully ")
            return redirect('test')
    else:
        form = ScheduleAppointmentForm()

    context = {'form': form}
    return render(request, 'doctor/sc_doctor.html', context)


@login_required(login_url='/')
def todays_schedule(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        appointments = Appointment.objects.filter(date=date)
        context = {'appointments': appointments}
        return render(request, 'doctor/ts.html', context)

    return render(request, 'doctor/ts.html')

@login_required(login_url='/')
def deal_detail(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            doctor = form.cleaned_data['doctor']
            product_name = form.cleaned_data['product_name']
            quantity_ordered = form.cleaned_data['quantity_ordered']
            entered_by = form.cleaned_data['entered_by']

            deal = Deal(
                doctor=doctor,
                product_name=product_name,
                quantity_ordered=quantity_ordered,
                entered_by=entered_by
            )
            deal.save()

            messages.success(request," Deal Done Succesfully ")
            return redirect('test')



    else:
        form = DealForm()

    context = {'form': form}
    return render(request, 'doctor/deal_detail.html', context)

@login_required(login_url='/')
def admin_deal(request):
    if request.method == 'POST':
        form = DoctorVisitsForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee_name']
            month = form.cleaned_data['month']
            
            visits_data = Deal.objects.filter(entered_by=employee).values('entered_by').annotate(total_appointments=Count('id'))
            
            return render(request, 'doctor/doctor_visits.html', {'visits_data': visits_data, 'emp':employee.username})

    else:
        form = DoctorVisitsForm()

    return render(request, 'doctor/doctor_visits_form.html', {'form': form})

@login_required(login_url='/')
def admin_deal_visit(request):
    if request.method == 'POST':
        form = visitDoctorVisitsForm(request.POST)
        if form.is_valid():
            # doctor = form.cleaned_data['doctor_name']
            employee = form.cleaned_data['employee_name']
            month = form.cleaned_data['month']
            
            visits_data = Appointment.objects.filter(entered_by=employee, date__month=month).values('entered_by').annotate(total_appointments=Count('id'))
            
            return render(request, 'doctor/aa1doctor_visits.html', {'visits_data': visits_data, 'doc':employee.username})

    else:
        form = visitDoctorVisitsForm()

    return render(request, 'doctor/aa2doctor_visits_form.html', {'form': form})




