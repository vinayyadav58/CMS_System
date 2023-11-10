from django.shortcuts import render, redirect,get_object_or_404
from .forms import AddProductForm
from .models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from doctor.models import Appointment,Deal



@login_required(login_url='/')
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            product_name = form.cleaned_data['product_name']
            company_name = form.cleaned_data['company_name']
            product_image = form.cleaned_data['product_image']
            product_price = form.cleaned_data['product_price']
            entered_by = form.cleaned_data['entered_by']
            
            product = Product(
                product_name=product_name,
                company_name=company_name,
                product_image=product_image,
                product_price=product_price,
                entered_by=entered_by
            )
            product.save()
            
            messages.success(request," Product added successfully ")
            return redirect('viewproducts')
    else:
        form = AddProductForm()

    return render(request, 'products/add_product.html', {'form': form})

def success(request):
    return render(request, 'products/success.html')

@login_required(login_url='/')
def test(request):
        products_count = Product.objects.all().count()
        user_count = User.objects.all().count()
        Appointment_count = Appointment.objects.all().count()
        deal_count = Deal.objects.all().count()
        context = {
            "products_count":products_count,
            "user_count":user_count,
            "Appointment_count":Appointment_count,
            "deal_count":deal_count,
        }
        return render(request,'base/base.html',context)

@login_required(login_url='/')
def view_products(request):
    products = Product.objects.all()
    return render(request, 'products/view_products.html', {'products': products})


@login_required(login_url='/')
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.product_name = form.cleaned_data['product_name']
            product.company_name = form.cleaned_data['company_name']
            product.product_image = form.cleaned_data['product_image']
            product.product_price = form.cleaned_data['product_price']
            product.entered_by = form.cleaned_data['entered_by']
            product.save()
            
            messages.success(request,"updated successfully ")
            return redirect('viewproducts')
            # return redirect('test')
    else:
        form = AddProductForm(initial={
            'product_name': product.product_name,
            'company_name': product.company_name,
            'product_price': product.product_price,
            'product_image': product.product_image,
            'entered_by': product.entered_by,
        })

    return render(request, 'products/update_product.html', {'form': form, 'product': product})

@login_required(login_url='/')
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request,"Deleted successfully ")
    return redirect('viewproducts')

