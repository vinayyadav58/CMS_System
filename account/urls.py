from django.contrib import admin
from django.urls import path,include
from account.views import myloginview,mylogout,register,view_products,emp_detail,delete_emp,update_emp
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

path('register/',register,name='register-page'),
    path('view_all/',view_products,name='view-all'),
    path('emp_detail/',emp_detail,name='emp_detail'),
    path('emp/delete/<int:pk>/', delete_emp, name='delete_emp'),
    path('emp/update/<int:pk>/', update_emp, name='update_emp'),


]