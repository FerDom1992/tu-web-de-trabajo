from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'core/base.html'

class BuscarTrabajoView(TemplateView):
    template_name = 'core/buscar_trabajo.html'

class AcercaDeView(TemplateView):
    template_name = 'core/acerca_de.html'

class ContactoView(TemplateView):
    template_name = 'core/contacto.html'