from django.contrib import admin
from erp.core.models import Type, Configuration, Product, Material, TouWen, Machine

admin.site.register(Configuration)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(Material)
admin.site.register(TouWen)

class MachineAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        # custom stuff here
        print 'aaaaa'
        obj.save()

admin.site.register(Machine, MachineAdmin)