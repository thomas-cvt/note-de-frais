from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mark_as_refunded/', views.mark_as_refunded, name='mark_as_refunded'),
    path('change_filter/', views.change_filter, name='change_filter'),
    path('select_categories/', views.select_categories, name='select_categories'),
]