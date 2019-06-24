from django.urls import path
from .views import HomePageView, BuscarTrabajoView, AcercaDeView, ContactoView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('buscar_trabajo/', BuscarTrabajoView.as_view(), name = 'buscar_trabajo'),
    path('acerca_de/', AcercaDeView.as_view(), name = 'acerca_de'),
    path('contacto/', ContactoView.as_view(), name = 'contacto'),
]
