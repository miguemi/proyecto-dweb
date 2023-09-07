from django.test import TestCase

from app.wsgi import *
from core.base.models import *

# LISTAR

print('Categorias:')
for i in Category.objects.filter():
    print(i)

# Create your tests here.
