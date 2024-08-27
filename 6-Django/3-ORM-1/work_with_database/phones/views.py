from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_dict = {'name':'name', 'min_price':'-price', 'max_price':'price'}
    if 'sort' in request.GET and request.GET['sort'] in sort_dict.keys():
        sort = sort_dict[request.GET.get('sort')]
    else:
        sort = 'name'
    context = {'phones': Phone.objects.all().order_by(sort)}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
