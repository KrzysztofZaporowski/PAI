from django.urls import path
from . import views

app_name = 'repository'

urlpatterns = [
    path('', views.DatabaseListView.as_view(), name='list'),
    path('<int:pk>/', views.DatabaseDetailView.as_view(), name='detail'),
    path('new/', views.DatabaseCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.DatabaseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DatabaseDeleteView.as_view(), name='delete'),
    path('<int:pk>/question/add/', views.QuestionCreateView.as_view(), name='question_add'),
    path('question/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='question_delete'),
    path('question/<int:pk>/answer/', views.AnswerCreateView.as_view(), name='answer_add'),
    path('answer/<int:pk>/delete/', views.AnswerDeleteView.as_view(), name='answer_delete'),
]
