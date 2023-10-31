from django import forms
from django.core.exceptions import ValidationError

class TableroForm(forms.Form):
    filas = forms.IntegerField(label='Número de Filas', min_value=1, max_value=20)
    columnas = forms.IntegerField(label='Número de Columnas', min_value=1, max_value=15)
    minas = forms.IntegerField(label='Número de Minas')

    def clean(self):
        cleaned_data = super().clean()
        filas = cleaned_data.get('filas')
        columnas = cleaned_data.get('columnas')
        minas = cleaned_data.get('minas')

        if minas > ((filas*columnas)/2):
            raise ValidationError(
                "El número de minas debe ser menor o igual al número total de casillas"
            )
        
        return cleaned_data


    

