from django.http import HttpResponse
from django.shortcuts import render
from iastatetheme.models import SiteTheme

from .models import Genus


def index(request):
    return render(request, 'lims/index.html')

def genera(request):
    genera_list = Genus.objects.all()
    context = {'genera_list': genera_list,
    }

    return render(request, 'genera/index.html', context)

