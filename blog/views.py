from django.utils import timezone
from django.shortcuts import  redirect
from django.core.mail import send_mail, BadHeaderError
from django.views import generic
from django.urls import reverse
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .models import Post
from .forms import FeedbackForm, PostForm
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

class FeedbackFormView(FormView):
    template_name = 'blog/feedback.html'
    form_class = FeedbackForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        subject = "Feedback from " + form.cleaned_data['name'] 
        from_email = form.cleaned_data['email']
        message =   form.cleaned_data['feedback'] + "\nEmail:" + form.cleaned_data['email']
        try:
            send_mail(subject, message, from_email, ['ahmed.allani@softcatalyst.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return super().form_valid(form)