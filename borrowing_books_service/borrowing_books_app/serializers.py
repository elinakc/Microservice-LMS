from rest_framework import serializers
from .models import Borrow

# SERIALIZER FOR BORROW
class BorrowSerializers(serializers.ModelSerializer):
  book_name = serializers.CharField(source ='book.book_name', read_only=True)
  borrow_username = serializers.CharField(source = 'user.username', read_only=True)
  
  
  class Meta:
        model = Borrow
        fields = "__all__"