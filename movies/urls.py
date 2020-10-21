from django.urls import path

from . import views

urlpatterns = [
    path("", views.Movies_views.as_view())
]