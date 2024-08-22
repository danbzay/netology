from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator
import logging

logger = logging.getLogger(__name__)

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_stations = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as file:
        bus_reader = csv.DictReader(file, delimiter=';')
        next(bus_reader)
        for row in bus_reader:
            bus_stations.append({
                'Name': row['Name'].split(',')[0], 
                'Street': row['Name'].split(',')[1].split('(')[0], 
                'District': row['District']
            })

    bus_stations_paged = Paginator(bus_stations, 10)    
    page_number = request.GET.get('page')
    if page_number is not None:
        page_number = int(page_number)
    else:
        page_number = 1
    
    context = {
        'bus_stations': bus_stations_paged.page(page_number).object_list,
        'page': bus_stations_paged.page(page_number),
    }
    logger.info(context)
    return render(request, 'stations/index.html', context)
