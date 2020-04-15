from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.FrontView.as_view(), name='home'),
]