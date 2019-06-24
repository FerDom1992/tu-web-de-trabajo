from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Post

class BuscarTrabajoArgView(ListView):
    model = Post
    paginate_by = 10


class BuscarTrabajoDetail(DetailView):
    model = Post