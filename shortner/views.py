from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        # still can process even just word without http.link.com
        if ("http://www" not in link) and ("https://www" not in link) :
            link = "http://www." + link + ".com"
        uid = str(uuid.uuid4())[:3] # give output 3 letter uid
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)
