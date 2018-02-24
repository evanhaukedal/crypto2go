from django.http import HttpResponse
from django.template.loader import get_template

def hello(response):

    return HttpResponse("hello")

def home(response):

    t = get_template('home.html')
    html = t.render()
    return HttpResponse(html)

