from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Operation
from datetime import datetime
from .functions import total

# Create your views here.

only_not_refunded = True

def home(request, extras={}):
    global only_not_refunded
    if only_not_refunded:
        operations = Operation.objects.filter(refunded=None).order_by("-date").values()
    else:
        operations = Operation.objects.order_by("-date").values()
    template = loader.get_template("index.html")
    context = {
        "operations": operations,
        "only_not_refunded": only_not_refunded,
        "total": total()
    }
    
    for param in extras.keys():
        context[param] = extras[param]

    return HttpResponse(template.render(context, request))

def mark_as_refunded(request):
    # https://www.section.io/engineering-education/how-to-build-templates-for-django-applications-with-htmx/
    Operation.objects.filter(refunded=None).update(refunded=datetime.now())
    extras = {
        "alert": True, 
        "date": datetime.now().strftime("%d/%m/%Y")
    }
    return home(request, extras=extras)

def change_filter(request):
    global only_not_refunded
    only_not_refunded = not only_not_refunded
    return home(request)