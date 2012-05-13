from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'projects$', 'akshaydeodotme.dashboard.views.projects'),
	url(r'academics$', 'akshaydeodotme.dashboard.views.academics'),
    url(r'$', 'akshaydeodotme.dashboard.views.index'),

)