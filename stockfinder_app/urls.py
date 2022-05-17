from django.urls import path
from  . import views
urlpatterns = [
    path('',views.get_home),
    path('search_result/',views.search_stock,name="search-result")
]