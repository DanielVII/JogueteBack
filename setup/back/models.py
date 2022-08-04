from django.db import models

class Personagem(models.Model):
    nome = models.CharField(max_length=20)
    url_img = models.CharField(max_length=1000)
    url_img_risadola = models.CharField(max_length=1000, blank=True)

    descricao = models.CharField(max_length=500)
    descricao_odio = models.CharField(max_length=666, blank=True)

    def __str__(self):
        return self.nome

class Habilidades(models.Model):
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)

    url_img_passiva = models.CharField(max_length=1000)
    url_img_arma = models.CharField(max_length=1000)
    url_img_um = models.CharField(max_length=1000)
    url_img_dois = models.CharField(max_length=1000)

    url_img_passiva_ativa = models.CharField(max_length=1000, blank=True)
    url_img_arma_ativa = models.CharField(max_length=1000, blank=True)
    url_img_um_ativa = models.CharField(max_length=1000, blank=True)
    url_img_dois_ativa = models.CharField(max_length=1000, blank=True)

    nome_passiva = models.CharField(max_length=20, blank=False, default="Habilas")
    nome_arma = models.CharField(max_length=20, blank=False, default="Habilas")
    nome_um = models.CharField(max_length=20, blank=False, default="Habilas")
    nome_dois = models.CharField(max_length=20, blank=False, default="Habilas")

    descricao_passiva = models.CharField(max_length=200, blank=False, default="Habilidade massa")
    descricao_arma = models.CharField(max_length=200, blank=False, default="Habilidade massa")
    descricao_um = models.CharField(max_length=200, blank=False, default="Habilidade massa")
    descricao_dois = models.CharField(max_length=200, blank=False, default="Habilidade massa")
    

