from django.urls import path
from products.views import add_product, success,test,view_products,update_product,delete_product

urlpatterns = [
    path('add-product/', add_product, name='add_product'),
    path('success/', success, name='success'),
    path('test/', test, name='test'),
    path('viewproducts/', view_products, name='viewproducts'),
    path('products/update/<int:pk>/', update_product, name='update_product'),
    path('products/delete/<int:pk>/', delete_product, name='delete_product'),
]
