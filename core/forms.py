from urllib import request

from django import forms

from core.models import Pessoa, Equipamento


class PessoaForm(forms.ModelForm):

    class Meta:  # Define os campos vindos do Model
        model = Pessoa
        fields = ('nome', 'usuario', 'ativo')

    def __init__(self, request, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(PessoaForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['nome'].widget = forms.TextInput(attrs={
            'placeholder': 'Nome',
            'title': 'Nome'})
        self.fields['usuario'].widget = forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'title': 'Usuario'})
        self.fields['nome'].label = ""
        self.fields['usuario'].label = ""


class EquipamentoForm(forms.ModelForm):

    class Meta:  # Define os campos vindos do Model
        model = Equipamento
        fields = ('descricao', 'ativo', 'idTipoEquipamento', 'idModelo')

    def __init__(self, request, *args, **kwargs):  # INIT define caracteristicas para os campos de formulário vindos do Model (banco de dados)
        super(EquipamentoForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['descricao'].widget = forms.TextInput(attrs={
            'placeholder': 'Descrição',
            'title': 'Descrição'})
        self.fields['descricao'].label = ""
