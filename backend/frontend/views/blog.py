from django.urls import reverse_lazy
from django.views.generic import (
    ListView as BaseListView, DetailView as BaseDetailView, CreateView as BaseCreateView, UpdateView as BaseUpdateView, DeleteView as BaseDeleteView
)
from backend.blog.models import Blog


class ListView(BaseListView):
    model = Blog
    template_name = "business/storefront/blog/list.html"


class DetailView(BaseDetailView):
    model = Blog
    template_name = "business/storefront/blog/detail.html"


class createView(BaseCreateView):
    model = Blog
    template_name = "business/storefront/blog/create.html"
    fields = [
        'name',
        'author',
        'description',
        'image',
    ]
    success_url = reverse_lazy('storefront:list')


class updateView(BaseUpdateView):
    model = Blog
    template_name = "business/storefront/blog/update.html"
    fields = [
        'name',
        'author',
        'description',
        'image',
    ]
    success_url = reverse_lazy('storefront:list')


class DeleteView(BaseDeleteView):
    model = Blog
    template_name = "business/storefront/blog/delete.html"
    success_url = reverse_lazy('storefront:list')
