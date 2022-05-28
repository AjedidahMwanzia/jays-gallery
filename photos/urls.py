from django.urls import path, re_path as url
from . import views


urlpatterns = [
    path('',views.gallery ,name= 'gallery'),
    path('photo/<str:pk>',views.viewPhoto ,name= 'photo'),
    path('search/',views.search_results,name='search_results'),
     url(r'^location/(\d+)', views.get_location, name='get_location')
]