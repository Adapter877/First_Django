from django.urls import path
from s1_app import views
urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('register',views.register),
    path('report',views.report),
    path('edit/<person_id>',views.edit),
    path('delete/<person_id>',views.delete),
]