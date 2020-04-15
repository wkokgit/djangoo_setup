from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from django.views import generic

class FrontView(generic.DetailView):
    template_name = 'index.html'
