from django.urls import path

from .views import BuscarTrabajoArgView, BuscarTrabajoDetail

urlpatterns = [
    path('buscar_trabajo/argentina/', BuscarTrabajoArgView.as_view(), name = 'buscar_trabajo_argentina'),
    path('<int:pk>/', BuscarTrabajoDetail.as_view(), name='buscar_trabajo_detail'),
]
