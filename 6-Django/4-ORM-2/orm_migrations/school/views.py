from django.views.generic import ListView
from django.shortcuts import render
from school.models import Student, Teacher
from django.db import connection, reset_queries
from django.conf import settings

def students_list(request):
    template = 'school/students_list.html'
    q = connection.queries
    context = {'students': Student.objects.prefetch_related(
                                           'teachers').all().order_by('name'),
               'sql': connection,
               'DEBUG': settings.DEBUG,
               'q': q}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
