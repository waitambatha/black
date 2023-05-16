from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('websites',views.websites, name='websites'),
    path('application', views.application,name='application'),
    path('cyber_security', views.cyber_security,name='cyber_security'),
    path('database', views.database,name='database'),
    path('profolio',views.profolio,name='profolio'),
    path('software', views.software, name='software')

]
