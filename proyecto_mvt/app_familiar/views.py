from re import template
from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from app_familiar.models import Familiar

def family_list_web(request):
    family_list = Familiar.objects.all()
    dictionary = {"relatives": family_list}
    template = loader.get_template('family_template.html')
    html_document = template.render(dictionary)
    return HttpResponse(html_document)
