from django import forms

from website.funcoes import verificarImagem
from website.models import Empresa


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu usuário.'}),
        error_messages={'required': 'Usuário não pode ser vazio'},
        label='Usuário'
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
        error_messages={'required': 'Senha não pode ser vazia'},
        label='Senha'
    )


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['razao_social', 'cnpj', 'data_abertura', 'cep', 'endereco', 'email', 'telefone', 'whatsapp',
                  'link_instagram', 'link_facebook', 'link_saf_google', 'logotipo', 'color', 'carousel1', 'carousel2', 'carousel3']

    razao_social = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nome da Empresa'}),
        error_messages={'required': 'Razao social não pode ser vazio'},
        label='Nome da Empresa'
    )

    cnpj = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'CNPJ/CPF da Empresa'}),
        error_messages={'required': 'CNPJ/CPF não pode ser vazio'},
        label='CNPJ/CPF da Empresa'
    )

    data_abertura = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={
                               'class': 'form-control', 'placeholder': 'Data de Abertura', 'type': 'date', }),
        error_messages={'required': 'Data de Abertura não pode ser vazio'},
        label='Data de Abertura da Empresa'
    )

    cep = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'CEP da Empresa'}),
        error_messages={'required': 'CEP não pode ser vazio'},
        label='CEP da Empresa'
    )

    endereco = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'ENDEREÇO da Empresa'}),
        error_messages={'required': 'ENDEREÇO não pode ser vazio'},
        label='ENDEREÇO da Empresa'
    )

    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'EMAIL da Empresa'}),
        error_messages={'required': 'EMAIL não pode ser vazio'},
        label='EMAIL da Empresa'
    )

    telefone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'CONTATO da Empresa'}),
        error_messages={'required': 'CONTATO não pode ser vazio'},
        label='CONTATO da Empresa'
    )

    whatsapp = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'WHATSAPP da Empresa'}),
        error_messages={'required': 'WHATSAPP não pode ser vazio'},
        label='WHATSAPP da Empresa'
    )

    link_instagram = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'INSTAGRAM da Empresa'}),
        error_messages={'required': 'INSTAGRAM não pode ser vazio'},
        label='INSTAGRAM da Empresa'
    )

    link_facebook = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'FACEBOOK da Empresa'}),
        error_messages={'required': 'FACEBOOK não pode ser vazio'},
        label='FACEBOOK da Empresa'
    )

    link_saf_google = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Link Satisfação Google da Empresa'}),
        error_messages={
            'required': 'Link Satisfação Google não pode ser vazio'},
        label='Link Satisfação Google'
    )

    logotipo = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='Logotipo da Empresa',
        validators=[verificarImagem]
    )

    color = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-color',
                               'placeholder': 'Cor Principal', 'type': 'color', }),
        error_messages={'required': 'A cor não pode ser vazia'},
        label='Cor Principal'
    )

    carousel1 = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='carousel1 da Homepage',
        validators=[verificarImagem]
    )

    carousel2 = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='carousel2 da Homepage',
        validators=[verificarImagem]
    )

    carousel3 = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='carousel3 da Homepage',
        validators=[verificarImagem]
    )


class EmailForm(forms.Form):
    to_email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Informe seu email'}),
        error_messages={
            'required': 'O email não pode ser vazio'},
        label='Informe seu email'
    )
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
        error_messages={
            'required': 'O nome não pode ser vazio'},
        label='Digite seu nome'
    )
    message = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite sua mensagem', 'type': 'textarea'}),
        error_messages={
            'required': 'A mensagem não pode ser vazia'},
        label='Digite sua mensagem'
    )
