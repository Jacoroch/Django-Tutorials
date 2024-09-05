from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.

class homePageView(TemplateView):
    template_name='pages/home.html'
    
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context
    

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact Us - Online Store",
            "subtitle": "Contacto",
            "email": "contacto@onlinestore.com",
            "address": "Calle Mugiwara, Wano Island",
            "phone": "+123 456 789",
        })
        return context



class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV","price": 500},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 1100},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 99},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 700},
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            product = Product.products[int(id) - 1]
        except (IndexError, ValueError):
            # Redirige a home si el ID no es válido
            return HttpResponseRedirect(reverse('home'))

        viewData = {
            "title": product["name"] + " - Online Store",
            "subtitle": product["name"] + " - Product information",
            "product": product,
        }
        return render(request, self.template_name, viewData)

    
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {
            "title": "Create product",
            "form": form,
        }
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Procesa el formulario y redirige si es necesario
            return redirect('form')
        else:
            viewData = {
                "title": "Create product",
                "form": form,
            }
            return render(request, self.template_name, viewData)

