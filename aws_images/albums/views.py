from django.shortcuts import render
from .models import Album
from django.views.generic import ListView, CreateView
from .forms import AlbumsForm

# Create your views here.


class AlbumsListView(ListView):
    model = Album
    template_name = 'albums/list.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        form = AlbumsForm()
        context = super().get_context_data(*args, **kwargs)
        context['form'] = form

        return context


class AlbumsCreateView(CreateView):
    model = Album
    form_class = AlbumsForm



