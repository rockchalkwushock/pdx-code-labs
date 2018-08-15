from django.urls import path
from . import views


app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('check_out/<title>', views.check_out, name='check_out')
]
