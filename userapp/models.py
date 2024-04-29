

from django.db import models


# Create your models here.
# contact
    
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def str(self):
        return self.full_name