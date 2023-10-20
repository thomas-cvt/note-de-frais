from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Operation, Category
from datetime import datetime
from .functions import total


# Create your views here.


def home(request, extras={}):
    operations = Operation.objects.filter(refunded=None).order_by("-date")
    categories = Category.objects.all()
    template = loader.get_template("index.html")
    context = {
        "operations": operations,
        "categories": categories,
        "total": total(),
    }
    for param in extras.keys():
        context[param] = extras[param]

    return HttpResponse(template.render(context, request))


def mark_as_refunded(request):
    # https://www.section.io/engineering-education/how-to-build-templates-for-django-applications-with-htmx/
    Operation.objects.filter(refunded=None).update(refunded=datetime.now())
    extras = {
        "alert": True,
        "date_of_refund": datetime.now().strftime("%d/%m/%Y")
    }
    return home(request, extras=extras)


def change_filter(request):
    template = loader.get_template("accordion.html")
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "total": total()
    }
    if request.POST.get("only_refunded"):
        context["operations"] = Operation.objects.filter(refunded=None).order_by("-date")
    else:
        context["operations"] = Operation.objects.order_by("-date")
    return HttpResponse(template.render(context, request))


def select_categories(request):
    Operation.objects.all()
    print(request.POST.getlist("categories")) # On sait qui est coché mais pas qui ne l'est pas
    return home(request)