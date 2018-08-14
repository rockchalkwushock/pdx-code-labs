from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Book


def index(request):
    context = {'books': Book.objects.all().order_by('author')[::-1]}
    return render(request, 'libraryapp/index.html', context)


def checked(request, title):
    book = Book.objects.get(title=title)
    if book.checked_out:
        book.checked_out = False
    else:
        book.checked_out = True
    book.save()
    return HttpResponseRedirect(reverse('library:index'))
