from django.urls import path
from . import views

urlpatterns = [
    path("", views.content_pages, name = "gi-content-pages"),
]
