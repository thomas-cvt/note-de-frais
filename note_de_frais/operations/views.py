from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Operation
from datetime import datetime
# Create your views here.

def home(request, extras={}):
    operations = Operation.objects.order_by("-date").values()
    template = loader.get_template("index.html")
    context = {
        "operations": operations
    }
    for param in extras.keys():
        context[param] = extras[param]
    return HttpResponse(template.render(context, request))

def mark_as_refunded(request):
    # https://www.section.io/engineering-education/how-to-build-templates-for-django-applications-with-htmx/
    # add contact
    Operation.objects.filter(refunded=None).update(refunded=datetime.now())
    return home(request, extras={"alert": True, "date": datetime.now().strftime("%d/%m/%Y")})

