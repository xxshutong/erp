# coding: utf-8
from datetime import timedelta
from django.contrib import admin
from erp.core.models import Type, Configuration, Product, Material, TouWen, Machine

admin.site.register(Configuration)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(Material)
admin.site.register(TouWen)


class MachineAdmin(admin.ModelAdmin):
    readonly_fields = ('daily_output_estimated', 'end_time_estimated_format', 'length_available')

    def save_model(self, request, machine, form, change):
        # custom stuff here
        if machine.speed and machine.wei_mi and machine.efficiency:
            machine.daily_output_estimated = machine.speed / machine.wei_mi * 60 / 100 * 24 * machine.efficiency
        if machine.length and machine.take_up_rate:
            machine.length_available = machine.length * (1 - machine.take_up_rate)
        # if machine.daily_output_estimated and machine.length_available and machine.start_time:
        #     interval = machine.length_available / machine.daily_output_estimated \
        #         if machine.length_available % machine.daily_output_estimated == 0 \
        #         else machine.length_available / machine.daily_output_estimated + 1
        #     machine.end_time_estimated = machine.start_time + timedelta(days=interval)

        machine.save()


admin.site.register(Machine, MachineAdmin)