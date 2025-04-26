from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=0)
    tags = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title
    
