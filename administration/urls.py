from django.contrib import admin
from django.urls import include, path
from . import views 

urlpatterns = [
    path("admin1",views.admin1),
    path("admin2",views.admin2),
    path(' ', views.addition),

]