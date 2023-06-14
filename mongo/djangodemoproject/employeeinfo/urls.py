from django.urls import path
from .views import *
urlpatterns = [
    path('get_departmentview/', DepartmentView.as_view()) ,
    path('get_departmentview/<int:id>/', DepartmentView.as_view()) 
]
