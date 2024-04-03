from .models import books
from rest_framework import serializers

class bookserializers(serializers.ModelSerializer):
  
  class Meta:
    model = books
    fields = "__all__"
    
  # def validate_isbn(self, value):
  #   if not value.isdigit() or len(value)!= 13:
  #     raise serializers.ValidationError("ISBN number must be digit and length should be at least thirteen ")
  #   return value
  
  