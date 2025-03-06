from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .models import Projetos, Colaboradores

from .serializers import ProjetoSerializer, ColaboradorSerializer


class ProjetoFormView(APIView):
    """
    Retorna os campos necessários para cadastrar um novo projeto.

    [GET] /projetos/form/
    """
    def get(self, request):
        fields = ["projeto", "id_financiador", "id_area_tecnologica", "coordenador", 
                  "ativo", "inicio_vigencia", "fim_vigencia", "valor", "qtd_membros", "id_colaboradores"]
        return Response({"fields": fields}, status=status.HTTP_200_OK)
    

class ProjetoListView(generics.ListAPIView):
    """
    Retorna a lista de todos os projetos cadastrados.

    [GET] /projetos/listar/
    """
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer


class ProjetoCreateView(generics.CreateAPIView):
    """
    Cadastra um novo projeto no sistema.

    [POST] /projetos/cadastrar/
    """
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer


class ProjetoInativarView(APIView):
    """
    Inativa um projeto específico.

    [POST] /projetos/{id}/inativar/
    """
    def post(self, request, id):
        projeto = get_object_or_404(Projetos, id_projeto=id)
        projeto.ativo = False
        projeto.save()
        return Response({"message": "Projeto inativado com sucesso"}, status=status.HTTP_200_OK)
    

class ProjetoEditarView(generics.UpdateAPIView):
    """
    Edita um projeto existente.

    [PATCH] /projetos/{id}/editar/
    """
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer
    lookup_field = 'id_projeto'


class ProjetoDetailView(generics.RetrieveAPIView):
    """
    Retorna os detalhes de um projeto específico.

    [GET] /projetos/{id}/visualizar/
    """
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer
    lookup_field = 'id_projeto'


class ProjetoEquipeView(APIView):
    """
    Retorna a equipe (colaboradores) associada a um projeto.

    [GET] /projetos/{id}/equipe/
    """
    def get(self, request, id):
        projeto = get_object_or_404(Projetos, id_projeto=id)
        equipe = projeto.id_colaboradores.all()
        serializer = ColaboradorSerializer(equipe, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProjetoEquipeAtualizarView(APIView):
    """
    Atualiza a equipe de um projeto.

    [PATCH] /projetos/{id}/equipe/atualizar/
    """
    def patch(self, request, id):
        projeto = get_object_or_404(Projetos, id_projeto=id)
        colaboradores_ids = request.data.get("id_colaboradores", [])
        projeto.id_colaboradores.set(Colaboradores.objects.filter(id_colaborador__in=colaboradores_ids))
        return Response({"message": "Equipe atualizada com sucesso"}, status=status.HTTP_200_OK)


class ColaboradorListView(generics.ListAPIView):
    """
    Retorna a lista de todos os colaboradores cadastrados.

    [GET] /colaboradores/listar/
    """
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradorSerializer


class ColaboradorCreateView(generics.CreateAPIView):
    """
    Cadastra um novo colaborador no sistema.

    [POST] /colaboradores/cadastrar/
    """
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradorSerializer


class ColaboradorDetailView(generics.RetrieveAPIView):
    """
    Retorna os detalhes de um colaborador específico.

    [GET] /colaboradores/{id}/visualizar/
    """
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradorSerializer
    lookup_field = 'id_colaborador'
    

class ColaboradorEditarView(generics.UpdateAPIView):
    """
    Edita um colaborador existente.

    [PATCH] /colaboradores/{id}/editar/
    """
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradorSerializer
    lookup_field = 'id_colaborador'