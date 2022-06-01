from django.urls import path
from . import views

urlpatterns = [
    #localhost:8000/my_app/
    path('', views.exmaple_view)
]