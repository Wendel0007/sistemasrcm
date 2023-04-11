from django.contrib import admin

from website.models import Empresa

# Register your models here.


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['id', 'razao_social', 'cnpj']
    list_display_links = ['id', 'razao_social']
    search_fields = ['id', 'razao_social', 'cnpj']
    list_per_page = 20
    ordering = ['-id']
