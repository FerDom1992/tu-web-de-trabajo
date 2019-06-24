from django.urls import path

from .views import BuscarTrabajoChView, BuscarTrabajoDetail

urlpatterns = [
    path('buscar_trabajo/chile/', BuscarTrabajoChView.as_view(), name = 'buscar_trabajo_chile'),
    path('<int:pk>/', BuscarTrabajoDetail.as_view(), name='buscar_trabajo_detail'),
]
