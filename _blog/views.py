from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

from datetime import datetime

# def home(request):
#     return render(request, 'home.html', {} )


class HomeView(ListView):
    model = Post
    template_name = "home.html"


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields= '__all__'
    # fields= ('title', 'body')

def all_posts_sorted_by_date(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'home.html', {'object_list': posts})

def all_authors(request):
    authors = Post.objects.values_list('author', flat=True).distinct()
    return render(request, 'all_authors.html', {'authors': authors})

def posts_by_author(request, author_name):
    posts = Post.objects.filter(author__username=author_name)
    return render(request, 'posts_by_author.html', {'author_name': author_name, 'posts': posts})

def posts_by_date(request):
    selected_date = request.GET.get('selected_date')
    try:
        selected_date = datetime.strptime(selected_date, '%Y-%m-%d')
        posts = Post.objects.filter(pub_date__date=selected_date)
    except:
        posts = []  # Handling of date formatting errors

    return render(request, 'posts_by_date.html', {'posts': posts, 'selected_date': selected_date})
