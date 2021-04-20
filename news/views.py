from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Headline


def index(request):
    latest_headline_list = Headline.objects.order_by('-pub_date')[:5]
    template = loader.get_template('news/index.html')
    context = {
        'latest_headline_list': latest_headline_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, headline_id):
    try:
        headline = Headline.objects.get(pk=headline_id)
    except Headline.DoesNotExist:
        raise Http404("Headline does not exist")
    return render(request, 'news/detail.html', {'headline': headline})
    

