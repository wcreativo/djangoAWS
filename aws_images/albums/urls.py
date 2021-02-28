from django.urls import path
from .views import AlbumsListView, AlbumsCreateView

app_name = 'albums'

urlpatterns = [
    path('', AlbumsListView.as_view(), name='list'),
    path('create/', AlbumsCreateView.as_view(), name='create')
]
