from django.urls import path

from . import views
from .controller import productcontroller

urlpatterns = [
    path("", views.view, name="index"),
    path("about/", views.about, name="about"),
    # path('create',productcontroller.)

]