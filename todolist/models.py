from django.db import models


# Create your models here.
class To_do(models.Model):
    subject=models.CharField(max_length=200,unique=True)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject
