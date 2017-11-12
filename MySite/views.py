from django.shortcuts import render
from MySite.models import Post
from django.utils import timezone

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'site/post_list.html', {
        'posts': posts
    })
