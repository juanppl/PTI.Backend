from django.db import models

# Create your models here.
class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category' 