from django.conf.urls import patterns, include, url
from django.contrib import admin
from solve.api import CalculatorResource, SessionResource
from tastypie.api import Api


admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CalculatorResource())
v1_api.register(SessionResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name="logout"),
    url(r'^', include('solve.urls')),
)
