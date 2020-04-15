from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<str:member>/', views.ContactsView.as_view(), name='contact'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]