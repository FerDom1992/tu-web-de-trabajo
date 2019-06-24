from django.urls import path

from .views import BuscarTrabajoMxView, BuscarTrabajoDetail

urlpatterns = [
    path('buscar_trabajo/mexico', BuscarTrabajoMxView.as_view(), name = 'buscar_trabajo_mexico'),
    path('<int:pk>/', BuscarTrabajoDetail.as_view(), name='buscar_trabajo_detail'),
]
