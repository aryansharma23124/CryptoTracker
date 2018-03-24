from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Cryptos

def Detail_Display (request):

    cryptos_detail = Cryptos.objects.order_by('id')
    template = loader.get_template('cryptodisplay/home.html')
    context = {
        'cryptos_detail': cryptos_detail,
    }


    return HttpResponse(template.render(context, request))

def get_log(request):
    cryptos_detail = Cryptos.objects.order_by('id')
    template = loader.get_template('cryptodisplay/table.html')
    context = {
        'cryptos_detail': cryptos_detail,
    }

    return HttpResponse(template.render(context, request))
