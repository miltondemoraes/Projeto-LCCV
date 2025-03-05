from django.contrib import admin
from .models import Financiadores, Colaboradores, AreasTecnologicas, Projetos

@admin.register(Financiadores)
class FinanciadoresAdmin(admin.ModelAdmin):
    list_display = ('id_financiados', 'financiador')
    search_fields = ('financiador',)

@admin.register(Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ('id_colaborador', 'nome', 'cpf', 'data_nascimento')
    search_fields = ('nome', 'cpf')

@admin.register(AreasTecnologicas)
class AreasTecnologicasAdmin(admin.ModelAdmin):
    list_display = ('id_area_tecnologica', 'area_tecnologica')
    search_fields = ('area_tecnologica',)

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('id_projeto', 'projeto', 'id_financiador', 'id_area_tecnologica', 'coordenador', 'ativo', 'inicio_vigencia', 'fim_vigencia', 'valor', 'qtd_membros')
    search_fields = ('projeto', 'coordenador')
    list_filter = ('ativo', 'id_area_tecnologica', 'id_financiador')
    filter_horizontal = ('id_colaboradores',)  # Para facilitar a seleção de múltiplos colaboradores