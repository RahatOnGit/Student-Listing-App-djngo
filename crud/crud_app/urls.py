from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('add_student/',views.add_student,name="add_student"),
    path('update_student/<str:pk>/',views.update_student,name="update_student"),
    path('delete_student/<str:pk>/',views.delete_student,name="delete_student"),
    path('delete_ok/<str:pk>/',views.delete_ok,name="delete_ok"),




]