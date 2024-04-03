from django.db import models


# Create your models here.
class Borrow(models.Model):
    user = models.IntegerField()
    book = models.IntegerField()
    due_date = models.DateField()
    borrowed_date = models.DateField(auto_now_add=True)
    returned_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.book


