from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views import generic
from .models import  Book

class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.all()

class DetailView(generic.DetailView):
    model=Book
    template_name = 'books/detail.html'

class SampleView(generic.DetailView):
    model = Book
    template_name = 'books/sample.html'

class BookCreate(CreateView):
    model = Book
    fields = '__all__'