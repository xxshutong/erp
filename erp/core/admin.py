from django.contrib import admin
from erp.core.models import Type, Configuration, Product, Material, TouWen, Machine

admin.site.register(Configuration)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(Material)
admin.site.register(TouWen)
admin.site.register(Machine)
