from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Operation

# Create your views here.

def home(request):
    operations = Operation.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        "operations": operations
    }
    return HttpResponse(template.render(context, request))
