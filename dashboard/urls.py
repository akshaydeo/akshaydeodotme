from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'projects$', 'akshaydeodotme.dashboard.views.projects'),
    url(r'$', 'akshaydeodotme.dashboard.views.index'),

)