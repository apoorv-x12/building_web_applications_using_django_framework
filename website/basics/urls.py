from django.urls import path, include
from . import views, ajax_views, author_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('wish/', views.wish),
    path('topics/', views.topics),
    # HTML and Django Forms
    path('interest/', views.interest),
    path('interest_post/', views.interest_post),
    path('interest_form/', views.interest_form),
    path('interest_form_custom/', views.interest_form_custom),
    # Ajax
    path('ajax/', ajax_views.ajax_demo),
    path('datetime/', ajax_views.send_datetime),
    # DB API
    path('authors/', author_views.list_authors),
    path('add_author/', author_views.add_author),
    path('add_author_form/', author_views.add_author_form),
]
