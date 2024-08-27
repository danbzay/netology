from django.shortcuts import render
from books.models import Book
from django.db.models import Q
from datetime import date
import re

def books_view(request, pub_date=''):
    template = 'books/books_list.html'
    f = Q()
    page = {'pub_date': pub_date}
    if re.match(r'^\d{4}-\d\d-\d\d$', pub_date):
        f &= Q(pub_date=pub_date)
        pub_dates = [_.pub_date for _ in Book.objects.all().order_by('pub_date')]
        pub_date_index = pub_dates.index(date.fromisoformat(pub_date))
        if pub_date_index > 0:
            page['has_prevous'] = True
            page['prevous_date'] = pub_dates[pub_date_index-1]
        if pub_date_index < len(pub_dates) - 1:
            page['has_next'] = True
            page['next_date'] = pub_dates[pub_date_index+1]


    context = {'books': Book.objects.filter(f), 'page': page}
    return render(request, template, context)
