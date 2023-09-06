from app.wsgi import *
from core.erp.models import Type

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
