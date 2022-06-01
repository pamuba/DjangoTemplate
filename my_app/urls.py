from django.urls import path
from . import views

#namespace name
app_name = 'my_app'

urlpatterns = [
    #localhost:8000/my_app/
    path('', views.exmaple_view, name="example"),
    path('variable/', views.variable_view, name="variable")
]