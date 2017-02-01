from django.forms import ModelForm
from .models import OpenSrcProject


class OpenSrcProjectForm(ModelForm):
    class Meta:
        model = OpenSrcProject
        exclude = ['pub_date', 'num_votes']