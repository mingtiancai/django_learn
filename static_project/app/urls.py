from django.urls import path,re_path
from . import views

urlpatterns=[
    path("",views.home),
    path("hello/",views.hello),
    # path('<year>/<int:month>/<slug:day>',views.data),
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html',views.date),
    re_path('(?P<year>[0-9]{4}).html',views.year,name='my_year'),
    re_path('dict/(?P<year>[0-9]{4}).htm',views.my_dict,{'month':'05'},name='my_dict'),
    path("download.html",views.download),
    path("google/",views.google),
    path("database/",views.get_data),
    path('login.html',views.login)
]