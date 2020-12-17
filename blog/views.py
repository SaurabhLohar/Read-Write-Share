from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .forms import CreateForm,UpdateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy


# Create your views here.

class PostCreate(CreateView):
    model = Post
    form_class = CreateForm
    template_name = 'blogs/post_blog.html'
    success_url = reverse_lazy('home')
    success_message = "Post was created successfully"

    @method_decorator(login_required(login_url='/account/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["blogs"] = Post.objects.filter(author=user)
        return context

class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'blogs/update_post.html'
    success_url = reverse_lazy('home')

    @method_decorator(login_required(login_url='/account/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["blogs"] = Post.objects.filter(author=user)
        return context

# def index(request):
# #     query = Post.objects.filter(status='public')
# #     template = 'blogs/index.html'
#     # return render(request,template,{'blogs':query})
#     return HttpResponse('djsd')
#
# def single_post(request,slug):
#     query = Post.objects.filter(slug=slug)
#     template = 'blogs/single_post.html'
#     context = {
#         'post':query
#     }
#     return render(request,template,context)
# #
class BlogsView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'blogs/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Post.objects.filter(status='public')
        context["siderbars"] = Post.objects.filter(status='public').order_by('?')[:3]
        return context

class SingleView(DetailView):
    model = Post
    template_name = 'blogs/single_post.html'
    context_object_name = 'post'
