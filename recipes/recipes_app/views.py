from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *
from .utils import DataMixin


def about(request):
    return HttpResponse(' Cooks recipes')

def add_page(request):
    return HttpResponse(' Cooks recipes')

def contact(request):
    return HttpResponse(' Cooks recipes')



class RecipesHome(DataMixin, ListView):
    model = Recipes
    template_name = 'recipes_app/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return context | c_def



class ShowPost(DataMixin,  DetailView):
    model = Recipes
    template_name = 'recipes_app/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return context | c_def