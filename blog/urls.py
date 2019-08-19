from django.urls import path, include
from . import views
# from .models import Blog

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.details, name='details')
]