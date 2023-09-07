from app.wsgi import *
from core.erp.models import Type, Employee

application = get_wsgi_application()

# query = Type.objects.all()
# print(query)

# insercion
# t = Type()
# t.name = 'Presidente'
# t.save()

#edicion
# t = Type.objects.get(pk=1)
# t.name = "prueba"
# t.save()

# #eliminacion
# t = Type.objects.get(pk=1)
# t.delete()

#filtrar
# obj = Type.objects.filter(name__contains='')
# obj = Type.objects.filter(name__icontains='') #busqueda ignorando mayusculas
# obj = Type.objects.filter(name__startswith='')
# obj = Type.objects.filter(name__endswith='')
# obj = Type.objects.filter(name__in=[])

# print(obj)

# emp = Employee.objects.filter(type_id=1)
