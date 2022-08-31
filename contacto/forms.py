from django import forms

class FormularioContacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)
    
    email=forms.CharField(label="Email", required=True)

    consulta=forms.CharField(label="Consulta", widget=forms.Textarea)