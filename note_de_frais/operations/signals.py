from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Operation, Category
from django.shortcuts import render
from django.template import loader
from .functions import total


@receiver([post_save, post_delete], sender=Operation)
def my_handler(sender, **kwargs):
    print("signal")
    template = loader.get_template("accordion.html")
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "total": total(),
        "operations": Operation.objects.order_by("-date")
    }
    return template.render(context)
