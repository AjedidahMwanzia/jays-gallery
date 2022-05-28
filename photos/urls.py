from django.urls import path
from . import views


urlpatterns = [
    path('',views.gallery ,name= 'gallery'),
    path('photo/<str:pk>',views.viewPhoto ,name= 'photo'),
    path('search/',views.search_results,name='search_results'),
    path('location/(\d+)', views.get_location, name='get_location'),
]