from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	return render_to_response("dashboard/index.html", {'tab_id' : '1'}, context_instance = RequestContext(request))

def projects(request):
	return render_to_response("dashboard/projects.html", {'tab_id' : '2'}, context_instance = RequestContext(request))

def academics(request):
	return render_to_response("dashboard/academics.html", {'tab_id' : '3'}, context_instance = RequestContext(request))

def accolades(request):
	return render_to_response("dashboard/accolades.html", {'tab_id' : '4'}, context_instance = RequestContext(request))

def publications(request):
        return render_to_response("dashboard/publications.html", {'tab_id' : '5'}, context_instance = RequestContext(request))

