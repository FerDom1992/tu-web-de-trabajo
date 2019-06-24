from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import PostMx

class BuscarTrabajoMxView(ListView):
    model = PostMx
    paginate_by = 10


class BuscarTrabajoDetail(DetailView):
    model = PostMx