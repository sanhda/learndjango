from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.all().order_by("date")
    template_name = 'blog/blog.html'
    context_object_name = 'Post'
    paginate_by = 1


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(pk)
    return render(request, "blog/post.html", {"post": post, "form": form})
