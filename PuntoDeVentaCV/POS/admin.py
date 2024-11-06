from django.contrib import admin

from .models import Producto
from .models import Distribuidor
from .models import Categoria
from .models import Marca

# Register your models here.

admin.site.register(Producto)
admin.site.register(Distribuidor)
admin.site.register(Categoria)
admin.site.register(Marca)