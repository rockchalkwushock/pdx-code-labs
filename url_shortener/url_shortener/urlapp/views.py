from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Url


def index(request):
    context = {'urls': Url.objects.all().order_by('-created_date')[:5]}
    return render(request, 'urlapp/index.html', context)


def save(request):
    if request.method == 'POST':
        url = request.POST['url_input']
        new_url = Url(url=url)
        new_url.save()
        return HttpResponseRedirect(reverse('urls:index'))


def redirect(request, code):
    url = Url.objects.get(code=code)
    return HttpResponseRedirect(url.url)
