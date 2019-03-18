from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
                    )
from . import views

urlpatterns = [

    path('', views.home, name='smartech-home'),
    path('home/', views.home, name='smartech-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('product/', views.product, name='smartech-product'),
    path('solution/', views.solution, name='smartech-solution'),
    path('service/', views.service, name='smartech-service'),
    path('blog/', PostListView.as_view(), name='smartech-blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]


