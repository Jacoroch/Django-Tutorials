from django.shortcuts import render
from django.views.generic import TemplateView
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


