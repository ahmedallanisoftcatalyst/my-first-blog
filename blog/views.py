from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse
from .models import Post
from .forms import PostForm
class PostList(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreate(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    def get_success_url(self):
        return reverse('post_detail',args=(self.object.id,))
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        self.object = form.save()
        return super().form_valid(form)

class PostUpdate(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    def get_success_url(self):
        return reverse('post_detail',args=(self.object.id,))
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        self.object = form.save()
        return super().form_valid(form)