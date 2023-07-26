from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView,  all_posts_sorted_by_date, all_authors, posts_by_author

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('all_posts_sorted_by_date/', all_posts_sorted_by_date, name="all_posts_sorted_by_date"),
    path('authors/', all_authors, name='all_authors'),
    path('posts_by_author/<str:author_name>/', posts_by_author, name='posts_by_author'),
    path('posts_by_date/', views.posts_by_date, name='posts_by_date'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
