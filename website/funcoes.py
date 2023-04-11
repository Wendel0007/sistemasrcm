import os

from django.conf import settings
from django.core.exceptions import ValidationError
from PIL import Image


def verificarImagem(arquivo):
    caminho_arquivo = os.path.splitext(arquivo.name)
    extensao_arquivo = caminho_arquivo[1].lower()
    extensoes_validas = ['.jpg', '.jpeg', '.png', '.svg']

    if extensao_arquivo not in extensoes_validas:
        raise ValidationError('Tipo de arquivo não suportado', code='invalid')


def redimensionar_imagem(imagem, newWidth=800, quality=50):
    if imagem:
        caminho_arquivo = os.path.join(settings.MEDIA_ROOT, imagem.name)
        imagem = Image.open(caminho_arquivo)
        width, height = imagem.size

        if width > newWidth:
            height = (height * newWidth) / width
            width = newWidth

        width = round(width)
        height = round(height)

        imagem_redimensionada = imagem.resize((width, height), Image.LANCZOS)
        imagem_redimensionada.save(
            caminho_arquivo, optimize=True, quality=quality)

        imagem.close()
        imagem_redimensionada.close()
