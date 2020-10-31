
from django.urls import path
from . import views
from .rest import rest_views,client_views

urlpatterns = [
    path('home/', views.book_home),
    path('list/', views.book_list),
    path('add/', views.book_add),
    path('delete/<int:id>', views.book_delete),
    path('edit/<int:id>', views.book_edit),
    path('search/', views.book_search),
    path('dosearch/', views.book_do_search),
    # REST API views
    path('rest/books/', rest_views.process_books),
    path('rest/books/<int:id>', rest_views.process_one_book),
    path('rest/client', client_views.add_book),

]
