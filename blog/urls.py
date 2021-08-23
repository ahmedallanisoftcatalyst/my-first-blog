from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.PostCreate.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdate.as_view(), name='post_edit'),
]