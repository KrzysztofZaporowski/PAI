from django.urls import path
from . import views

app_name = 'repository'

urlpatterns = [
    path('', views.DatabaseListView.as_view(), name='list'),
    path('<int:pk>/', views.DatabaseDetailView.as_view(), name='detail'),
    path('new/', views.DatabaseCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.DatabaseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DatabaseDeleteView.as_view(), name='delete'),
]
