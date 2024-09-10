from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/create/', ProductCreateView.as_view(), name='form'),
    path('products/created/', TemplateView.as_view(template_name="products/product_created.html"), name='product_created'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>/', CartView.as_view(), name='cart_add'),
    path('cart/removeAll/', CartRemoveAllView.as_view(), name='cart_removeAll'),
]