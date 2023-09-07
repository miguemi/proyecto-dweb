from django.db import models
from datetime import datetime
from core.base.choices import gender_choices

# Create your models here

# Categorias
class Category(models.Model):
    name = models.TextField(verbose_name='Nombre', unique=True)


    def __str__(self) -> str:
        return 'Nombre: {}'.format(self.name)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

# Producto
class Product(models.Model):
    name = models.TextField(verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

# Cliente     
class Client(models.Model):
    names = models.TextField(verbose_name='Nombres')
    surnames = models.TextField(verbose_name='Apellidos')
    dni = models.TextField(unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.TextField(null=True, blank=True, verbose_name='Dirección')
    sexo = models.TextField(choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self) -> str:
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

#Venta
class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    def __str__(self) -> str:
        return self.cli.names


    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']

# detalle de las ventas
class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self) -> str:
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalle de ventas'
        ordering = ['id']
