from django.urls import include, path
from .import views
urlpatterns = [
    path('',views.home,name ='gallery-home'),
    path('search', views.filter_by_search, name="gallery-search")
]
