from django.db import models
from djongo.models import ObjectIdField


class Todos(models.Model):
    _id = ObjectIdField()  # MongoDB's default primary key
    name = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    # assigned_users = models.ManyToManyField('auth.User', related_name='assigned_samples', blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'todos'
        
         
         
         
         
         