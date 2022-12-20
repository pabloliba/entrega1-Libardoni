from django import forms

class formempleado(forms.Form):
    nombre= forms.CharField(label='nombre empleado', max_length=50)
    documento=forms.IntegerField(label='documento')
