from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
from .models import Book, Card


@login_required
def index(request):
    context = {
        # 'books': Book.objects.all().order_by('author')[::-1],
        'books': Book.objects.filter(checked_out=False).order_by('author')[::-1],
        'my_books': Card.objects.get(user=request.user)
    }
    return render(request, 'libraryapp/index.html', context)


@login_required
def check_out(request, title):
    book = Book.objects.get(title=title)
    card = Card.objects.get(user=request.user)
    if book.checked_out:
        book.checked_out = False
        card.checked_out = False
        book.save()
        card.save()
    else:
        book.checked_out = True
        card.checked_out = True
        card.book = book
        card.timestamp = datetime.now()
        book.save()
        card.save()
    return HttpResponseRedirect(reverse('library:index'))
