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

    def __str__(self):
        return self.title
    
