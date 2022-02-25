
from django.shortcuts import render
from django.utils import timezone

from blog.serializer import PostSerializer
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__gte=timezone.now()).order_by('published_date')
    posts_2 = Post.objects.filter(delete_date__gte=timezone.now()).order_by('delete_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'posts_2':posts_2})


