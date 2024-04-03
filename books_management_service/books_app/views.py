from rest_framework import generics
from .serializers import bookserializers
from rest_framework.response import Response
from rest_framework import status
from books_app.tasks import send_borrow_notification
from .bookproducer import publish_borrow_book
from .bookproducer import publish_availability_check
from rest_framework.decorators import api_view
from .models import books
from django.contrib.auth.decorators import login_required

# Create your views here.

class BookListCreateAPIView(generics.ListCreateAPIView):
  queryset = books.objects.all()
  serializer_class = bookserializers
  
  
  def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        # book_id = request.data.get('book_id')
        # # Start Celery task to process the book
        # task_result = process_book.delay(book_id)
        # return Response({'task_id': task_result.id})
      
class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = books.objects.all()
    serializer_class = bookserializers
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    


@api_view(['POST'])
def check_availability(request):
    book_id = request.data.get('book_id')
    borrower_id = request.data.get('borrower_id')

    result = publish_availability_check(book_id, borrower_id)

    if result == 'sent':
        return Response({'message': 'Availability check sent'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Failed to send availability check'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['POST'])
# @login_required (login_url='http://127.0.0.1:8000/api/auth/login/')
def borrow_book(request):
    book_id = request.data.get('book_id')

    try:
        book = books.objects.get(id=book_id)

        if book.quantity_available <= 0:
            return Response({'message': 'Book not available for borrowing'}, status=status.HTTP_400_BAD_REQUEST)

        # Book is available, borrow it
        book.quantity_available -= 1
        book.save()
       
        # Trigger Celery task to send email notification asynchronously
        # send_borrow_notification.delay(request.user.email, book.title, '2024-04-10')  # Example return date
        
        publish_borrow_book(book_id)
        return Response({'message': 'Book borrowed successfully'}, status=status.HTTP_200_OK)
    
    except books.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    
