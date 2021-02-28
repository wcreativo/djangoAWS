from .models import Album
from django.forms import ModelForm


class AlbumsForm(ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'id': 'title',
            'placeholder': 'Titulo'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'id': 'description',
            'placeholder': 'Titulo'
        })



