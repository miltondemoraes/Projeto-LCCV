from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .models import Projetos, Colaboradores

from .serializers import ProjetoSerializer, ColaboradorSerializer


class ProjetoFormView(APIView):
    def get(self, request):
        fields = ["projeto", "id_financiador", "id_area_tecnologica", "coordenador", 
                  "ativo", "inicio_vigencia", "fim_vigencia", "valor", "qtd_membros", "id_colaboradores"]
        return Response({"fields": fields}, status=status.HTTP_200_OK)
    

class ProjetoListView(generics.ListAPIView):
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer


class ProjetoCreateView(generics.CreateAPIView):
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer


class ProjetoInativarView(APIView):
    def post(self, request, id):
        projeto = get_object_or_404(Projetos, id_projeto=id)
        projeto.ativo = False
        projeto.save()
        return Response({"message": "Projeto inativado com sucesso"}, status=status.HTTP_200_OK)
    

class ProjetoEditarView(generics.UpdateAPIView):
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer
    lookup_field = 'id_projeto'


class ProjetoDetailView(generics.RetrieveAPIView):
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer
    lookup_field = 'id_projeto'


class ProjetoEquipeView(APIView):
    def get(self, request, id):
        projeto = get_object_or_404(Projetos, id_projeto=id)
        equipe = projeto.id_colaboradores.all()
        serializer = ColaboradorSerializer(equipe, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProjetoEquipeAtualizarView(APIView):
    def patch(self, request, id):
        projeto = get_object_or_404(Projetos, id_projeto=id)
        colaboradores_ids = request.data.get("id_colaboradores", [])
        projeto.id_colaboradores.set(Colaboradores.objects.filter(id_colaborador__in=colaboradores_ids))
        return Response({"message": "Equipe atualizada com sucesso"}, status=status.HTTP_200_OK)


class ColaboradorListView(generics.ListAPIView):
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradorSerializer


class ColaboradorCreateView(generics.CreateAPIView):
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradorSerializer


class ColaboradorDetailView(generics.RetrieveAPIView):
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradorSerializer
    lookup_field = 'id_colaborador'
    

class ColaboradorEditarView(generics.UpdateAPIView):
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradorSerializer
    lookup_field = 'id_colaborador'