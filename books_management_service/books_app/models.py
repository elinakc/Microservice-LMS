from django.db import models

# Create your models here.
class books(models.Model):
  title = models.CharField(max_length = 100)
  author = models.CharField(max_length = 100)
  ISBN = models.CharField(max_length = 100)
  status = models.BooleanField(default=True)
  quantity_available = models.IntegerField(default=0)
  
  def __str__(self):
    return self.title
    
    