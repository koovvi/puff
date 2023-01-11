from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import ListView
from .models import Flower
from .forms import UploadFlower
from django.http.response import HttpResponse


class MyAccountView(CreateView):
    model = Flower
    template_name = 'user/profile.html'
    fields = '__all__'

def index(request):
    return render(request, 'main.html')

def catalog(request):
    flowers = Flower.objects.all()
    if request.method == 'GET':
        return render(request, 'catalog.html', {'flowers': flowers})

def uploadFlower(request):
    if request.method == "POST":
        form = UploadFlower(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    return render(request, 'addFlower.html', {'form': UploadFlower})
