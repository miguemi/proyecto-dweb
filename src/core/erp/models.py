from django.db import models
from datetime import datetime


class Type(models.Model):
    name = models.TextField(verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'empleado_tipo'
        ordering = ['id']

class Category(models.Model):
    
    name = models.TextField(verbose_name='Nombre')

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

            
# Create your models here.
class Employee(models.Model):
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.TextField(verbose_name='Nombres')
    dni = models.TextField(unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now) 
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    age = models.PositiveIntegerField()
    salary= models.DecimalField(default=0, max_digits=9, decimal_places=2)
    state = models.BooleanField()
    avatar = models.ImageField(upload_to='avatar/%Y/%m%/%d', null=True, blank=True)
    cvitae = models.ImageField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
