from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.PostCreate.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdate.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('feedback/', views.FeedbackFormView.as_view(), name='feedback'),
    path('thanks/', TemplateView.as_view(template_name="blog/thanks.html"), name='thanks')
]