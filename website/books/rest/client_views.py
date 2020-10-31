from django.shortcuts import render


def add_book(request):
    return render(request, 'rest/add_book.html')
