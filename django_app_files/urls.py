from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_piano", views.add_piano, name="add_piano"),
    path("piano_detail/<str:piano_brand>", views.piano_detail, name="piano_detail"),
    path("remove_piano/<str:piano_brand>", views.remove_piano, name="remove_piano"),
]
