from rest_framework import generics, status
from .bookproducer import publish_availability_check
from .serializers import BorrowSerializers
from .models import Borrow
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class BorrowListCreateAPIView(generics.ListCreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializers

class BorrowRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializers
    
    
@api_view(['POST'])
def check_availability(request):
    book_id = request.data.get('book_id')
    borrower_id = request.data.get('borrower_id')

    result = publish_availability_check(book_id, borrower_id)

    if result == 'sent':
        return Response({'message': 'Availability check sent'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Failed to send availability check'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


# class BorrowBookAPIView(APIView):
#     def post(self, request):
#         book_id = request.data.get('book_id')
#         borrower_id = request.user.id  # Assuming you have authentication set up
        
#         # Call the availability check producer to trigger an availability check with the Book Management Service
#         availability_check_result = publish_availability_check(book_id, borrower_id)
        
#         if availability_check_result == 'available':
#             # Book is available, create a Borrow record
#             borrow_data = {'book': book_id, 'borrower': borrower_id}
#             serializer = BorrowSerializers(data=borrow_data)
#             if serializer.is_valid():
#                 serializer.save()
                
#                 # # Publish a message to notify books_management_service about the borrowed book
#                 # publish_borrowed_book(book_id)
                
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             # Book is not available, return an error response
#             return Response({'error': 'Book is not available for borrowing'}, status=status.HTTP_400_BAD_REQUEST)

    
