from django.urls import path
from . import views
from .views import get_response
#app_name = 'Sec_App'


urlpatterns = [
    path('', views.home, name="home"),
    path('get-response/', get_response,name="get-response"),
    path('tools/',views.tools,name="tools"),
    path('port-scanning/',views.port_scanning,name="port_scanning"),
    path('csrf-detection/', views.csrf_detection, name="csrf_detection"),
    path('host-discovery/', views.host_discovery, name="host_discovery"),
    path('dos-detection/', views.dos, name="dos"),
    path('base/', views.base, name="base"),

]

#path('', views.home, name="home"),