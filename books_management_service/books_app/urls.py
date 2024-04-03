from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateAPIView.as_view(), name="book-list-create"),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view(), name="book-detail"),
   
    path('availability_check/', views.check_availability, name="book-check"),
    path('borrow_book/', views.borrow_book, name="borrow_book"),
]

