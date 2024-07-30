from django.db import models

from categories.models import Category

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    displayName = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Agregado max_digits y decimal_places
    isActive = models.BooleanField(default=True)
    creationDate = models.DateField(auto_now_add=True)  # Para establecer la fecha automáticamente al crear
    expireDate = models.DateField(null=True, blank=True)  # Permitir nulo y vacío
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)  # Relación de clave foránea
    availableQty = models.SmallIntegerField()
    lastModificationDate = models.DateField(auto_now=True)  # Para actualizar la fecha automáticamente al modificar
    isDeleted = models.BooleanField(default=False)
    deletedDate = models.DateField(null=True, blank=True)  # Permitir nulo y vacío

    def __str__(self):
        return self.fullName
    
    class Meta:
        db_table = 'product'