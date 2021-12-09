from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Empleados, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento_id',
        'job',
        'full_name',
        'id'
    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name', 'last_name')
    list_filter = ('job',)
    filter_horizontal = ('habilidades',)


admin.site.register(Empleados, EmpleadosAdmin)

