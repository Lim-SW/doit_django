#from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create use CBV
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/post_list.html'

class PostDetail(DetailView):
    model = Post

""" # CBV로 다시 만들거야.... 안녕 FBV....ㅠㅠ
def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/post_list.html',
        {
            'posts': posts
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk = pk)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
        }
    )
"""