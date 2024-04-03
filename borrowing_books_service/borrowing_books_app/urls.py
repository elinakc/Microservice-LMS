
from django.urls import path
from . import views

urlpatterns = [
    

path('borrow/', views.BorrowListCreateAPIView.as_view(), name='borrow_list'),
path('borrow/<int:pk>/', views.BorrowRetrieveUpdateDestroyAPIView.as_view(), name='borrow_detail'),

path('availability_check/', views.check_availability, name='availability_check'),

# path('borrow_book/', views.BorrowBookAPIView.as_view(), name='borrow_book'),
# path('return_book/', views.ReturnBookAPIView.as_view(), name='return_book'),
# path('borrow_book/', views.BorrowBookAPIView.as_view(), name='borrow_book'),
# path('consume-messages/', views.consume_messages, name='consume_messages'),
# path('return_book/<int:pk>/', views.ReturnBookView.as_view(), name='return_book'),
# path('notify_due/<int:pk>/', views.NotifyOverdueView.as_view(), name='notify'),

 ]