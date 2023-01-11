from django.forms import ModelForm
from .models import Client
class UploadFlower(ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'phone_number', 'client_adress', 'client_flower']