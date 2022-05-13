from django.urls import path
from .views import *

urlpatterns = [
    path('', RecipesHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('<slug:post_slug>/', ShowPost.as_view(), name='post'),
]