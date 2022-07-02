from django.urls import path
from ..views import blog
urlpatterns = [
    path('', blog.ListView.as_view(), name='list'),
    path('blog/<int:pk>/', blog.DetailView.as_view(), name='detail'),
    path('blog/add/', blog.createView.as_view(), name='create'),
    path('blog/<int:pk>/update', blog.updateView.as_view(), name='update'),
    path('blog/<int:pk>/delete', blog.DeleteView.as_view(), name='delete'),
]
