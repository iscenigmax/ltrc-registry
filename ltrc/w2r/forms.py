from django import forms
from .models import Registro


class RegistroForm(forms.ModelForm):
    tiempo_5k = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'HH:MM:SS'}))
    tiempo_10k = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'HH:MM:SS'}))
    tiempo_21k = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'HH:MM:SS'}))
    tiempo_42k = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'HH:MM:SS'}))

    class Meta:
        model = Registro
        fields = [
            'correo',
            'nombre',
            'apellidos',
            'edad',
            'sexo',
            'peso_kgs',
            'estatura',
            'telefono',
            'objetivo_5k',
            'tiempo_5k',
            'tiempo_10k',
            'tiempo_21k',
            'tiempo_42k',
            'confirmado',
        ]