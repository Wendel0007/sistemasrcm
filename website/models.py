from django.db import models


class Empresa(models.Model):
    razao_social = models.CharField(max_length=100, null=True, blank=True)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    data_abertura = models.DateField(null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    whatsapp = models.CharField(max_length=13, null=True, blank=True)
    link_instagram = models.CharField(max_length=255, null=True, blank=True)
    link_facebook = models.CharField(max_length=255, null=True, blank=True)
    link_saf_google = models.CharField(max_length=255, null=True, blank=True)
    logotipo = models.ImageField(
        upload_to='website/upload/%Y/%m/%d/', null=True, blank=True)
    color = models.CharField(max_length=10, null=True)
    carousel1 = models.ImageField(
        upload_to='website/upload/%Y/%m/%d/', null=True, blank=True)
    carousel2 = models.ImageField(
        upload_to='website/upload/%Y/%m/%d/', null=True, blank=True)
    carousel3 = models.ImageField(
        upload_to='website/upload/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.razao_social
