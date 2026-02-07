from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Library URLs
    path('libraries/', views.library_list, name='library_list'),
    path('libraries/create/', views.create_library, name='create_library'),
    path('libraries/delete/<int:library_id>/', views.delete_library, name='delete_library'),
    
    # Author URLs
    path('authors/', views.author_list, name='author_list'),
    path('authors/create/', views.create_author, name='create_author'),
    path('authors/update/<int:author_id>/', views.update_author, name='update_author'),
    path('authors/delete/<int:author_id>/', views.delete_author, name='delete_author'),
    
    # Book URLs
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/update/<int:book_id>/', views.update_book, name='update_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    
    # Member URLs
    path('members/', views.member_list, name='member_list'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/update/<int:member_id>/', views.update_member, name='update_member'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),
]
