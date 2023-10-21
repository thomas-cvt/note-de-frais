from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('mark_as_refunded/', views.mark_as_refunded, name='mark_as_refunded'),
    path('change_filter/', views.change_filter, name='change_filter'),
    path('select_categories/', views.select_categories, name='select_categories'),
    path('accounts/login/', LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
