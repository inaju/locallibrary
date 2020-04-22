from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns=[
    path('', views.index, name='index'),
    path('mitchel/', views.mitchel, name='mitchel'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/', views.AuthorListView.as_view(), name='author'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('home', views.home, name='home'),
    path('sendemail', views.sendemail, name='sendemail'),
    path('accounts/', include('django.contrib.auth.urls')),

    
    

    
]
