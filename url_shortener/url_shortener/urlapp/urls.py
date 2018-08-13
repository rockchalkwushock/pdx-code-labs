from django.urls import path
from . import views


app_name = 'urls'
urlpatterns = [
    path('', views.index, name='index'),
    path('save', views.save, name='save'),
    path('redirect/<code>', views.redirect, name='redirect')
]
