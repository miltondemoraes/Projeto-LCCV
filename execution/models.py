from django.db import models

class Financiadores(models.Model):
    id_financiados = models.AutoField(primary_key=True)
    financiador = models.CharField(max_length=100)

    def __str__(self):
        return self.financiador
    
class Colaboradores(models.Model):
    id_colaborador = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome + ": " + self.cpf
    
class AreasTecnologicas(models.Model):
    id_area_tecnologica = models.AutoField(primary_key=True)
    area_tecnologica = models.CharField(max_length=100)

    def __str__(self):
        return self.area_tecnologica
    
class Projetos(models.Model):
    id_projeto = models.AutoField(primary_key=True)
    projeto = models.CharField(max_length=100)
    id_financiador = models.ForeignKey(Financiadores, on_delete=models.PROTECT)
    id_area_tecnologica = models.ForeignKey(AreasTecnologicas, on_delete=models.PROTECT)
    coordenador = models.CharField(max_length=100)
    ativo = models.BooleanField()
    inicio_vigencia = models.DateField()
    fim_vigencia = models.DateField()  
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    qtd_membros = models.IntegerField()
    id_colaboradores = models.ManyToManyField(Colaboradores, related_name='colaboradores')

    def __str__(self):
        return self.titulo