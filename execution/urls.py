from django.urls import path
from .views import (
    ProjetoFormView, 
    ProjetoListView, 
    ProjetoCreateView, 
    ProjetoInativarView,
    ProjetoEditarView, 
    ProjetoDetailView, 
    ProjetoEquipeView, 
    ProjetoEquipeAtualizarView,
    ColaboradorListView, 
    ColaboradorCreateView, 
    ColaboradorDetailView, 
    ColaboradorEditarView
)


urlpatterns = [
    path('projetos/form/', ProjetoFormView.as_view(), name='projeto-form'),
    path('projetos/listar/', ProjetoListView.as_view(), name='projeto-listar'),
    path('projetos/cadastrar/', ProjetoCreateView.as_view(), name='projeto-cadastrar'),
    path('projetos/<int:id>/inativar/', ProjetoInativarView.as_view(), name='projeto-inativar'),
    path('projetos/<int:id_projeto>/editar/', ProjetoEditarView.as_view(), name='projeto-editar'),
    path('projetos/<int:id_projeto>/visualizar/', ProjetoDetailView.as_view(), name='projeto-visualizar'),
    path('projetos/<int:id>/equipe/', ProjetoEquipeView.as_view(), name='projeto-equipe'),
    path('projetos/<int:id>/equipe/atualizar/', ProjetoEquipeAtualizarView.as_view(), name='projeto-equipe-atualizar'),

    path('colaboradores/listar/', ColaboradorListView.as_view(), name='colaborador-listar'),
    path('colaboradores/cadastrar/', ColaboradorCreateView.as_view(), name='colaborador-cadastrar'),
    path('colaboradores/<int:id_colaborador>/visualizar/', ColaboradorDetailView.as_view(), name='colaborador-visualizar'),
    path('colaboradores/<int:id_colaborador>/editar/', ColaboradorEditarView.as_view(), name='colaborador-editar'),
]