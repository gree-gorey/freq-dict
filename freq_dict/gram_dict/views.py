from django.shortcuts import render

from django.http import Http404, HttpResponse, HttpResponseRedirect

def index(request):

    if request.POST:
		print request.POST['term']
		return HttpResponseRedirect("/")
    else:
		return render_to_response('index.html')
