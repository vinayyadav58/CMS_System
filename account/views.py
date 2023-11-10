from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import registrationForm,details_emp_form
from products.views import test
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, redirect,get_object_or_404





# Create your views here.


class myloginview(LoginView):
    def form_valid(self, form):
        messages.success(self.request,"Logged in successfully ")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request," invalid username or password  ")
        return super().form_invalid(form)
    
class mylogout(LogoutView):
    def get_next_page(self):
        messages.success(self.request,"logged out successfully ")
        return reverse_lazy('login')
    


@login_required(login_url='/')
def register(request):
    if request.method == 'GET':
         form = registrationForm()
         return render(request,'account/register.html',{'form_data':form})

    if request.method == 'POST':
         form = registrationForm(request.POST)
         if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request," Account created succesfully for user " + user_name )
            return redirect('test')

         else:
            messages.error(request,"OOPS some issue in your form")
            return render(request,'account/register.html',{'form_data':form})
        
    return render(request,'account/register.html',{'form_data':form})

def view_products(request):
    products = deatil_emp.objects.all()
    return render(request, 'account/view_employee.html', {'products': products})


@login_required(login_url='/')
def emp_detail(request):
        if request.method == 'POST':
             form = details_emp_form(request.POST,request.FILES)
             if form.is_valid():
                 first_name = form.cleaned_data['first_name']
                 last_name = form.cleaned_data['last_name']
                 email = form.cleaned_data['email']
                 Joining_date = form.cleaned_data['Joining_date']
                 activtiy= form.cleaned_data['activtiy']
            # form.save()
             d = deatil_emp(
                first_name=first_name,
                last_name=last_name,
                email=email,
                joining=Joining_date,
                status=activtiy,
                )
             d.save()
             messages.success(request,"New employee added succesfully ")
             return redirect('test')
        else:
            form = details_emp_form()
            context = {'form': form}
            return render(request, 'account/detail_emp.html', context)

@login_required(login_url='/')
def delete_emp(request, pk):
    emp = get_object_or_404(deatil_emp, pk=pk)
    emp.delete()
    messages.success(request,"Deleted successfully ")
    return redirect('test') 



@login_required(login_url='/')
def update_emp(request, pk):
    emp = get_object_or_404(deatil_emp, pk=pk)
    
    if request.method == 'POST':
        form = details_emp_form(request.POST, request.FILES)
        if form.is_valid():
            emp.first_name = form.cleaned_data['first_name']
            emp.last_name = form.cleaned_data['last_name']
            emp.email = form.cleaned_data['email']
            emp.joining = form.cleaned_data['Joining_date']
            emp.status = form.cleaned_data['activtiy']
            emp.save()
            
            messages.success(request,"updated successfully ")
            return redirect('view-all')
            # return redirect('test')
    else:
        form = details_emp_form(initial={
            'first_name': emp.first_name,
            'last_name': emp.last_name,
            'email': emp.email,
            'Joining_date': emp.joining,
            'activtiy': emp.status,
        })

    return render(request, 'account/update_emp.html', {'form': form, 'emp': emp})