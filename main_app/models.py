from django.db import models

# Create your models here.
class TodoModel(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    active= models.BooleanField(default=False)
    class Meta:  
        db_table = "ToDoTable"  
    
