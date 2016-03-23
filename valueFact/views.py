from django.shortcuts import render,get_object_or_404

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from valueFact.models import ValueFactPost

def valueFactList(request):
    valueFacts = ValueFactPost.published.all()
    return render(request, '/companies/valueFact/list.html', {'valueFacts': valueFacts})

def valueFact_detail(request, year, month, day, valueFact):
    valueFact = get_object_or_404(valueFact, slug=valueFact,
                                  status='published',
                                  publish__month=month,
                                  publish__day=day)
    return render(request, '/companies/valueFact/detail.html',
                  {'valueFact': valueFact})

