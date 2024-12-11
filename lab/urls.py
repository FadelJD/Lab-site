from django.urls import path
from . import views

app_name = 'lab'
urlpatterns = [
    path('<int:pk>/index', views.IndexView.as_view(), name='indexlove'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('<int:pk>/', views.Lab, name = 'Lab'),
    #path('<int:pk>/', views.Info, name = 'Info'),
    #path('<int:pk>/', views.Gallery, name = 'Gallery'),
    #path('<int:pk>/', views.News, name = 'News'),
]
