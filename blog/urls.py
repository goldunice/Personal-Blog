from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.allArticles, name="home"),
    path('detail/<int:article_id>/', views.detail, name="detail"),
]
