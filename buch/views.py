from django.shortcuts import render

from progress.buch.models import Book

def progress( request ):
    response_dict = { "books": Book.objects.all() }
    return render( request, "progress.html", response_dict)