from django.db import models
class Department(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='Department/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def str(self):
        return self.name 
# Create your models here.
