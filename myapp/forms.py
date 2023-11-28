from django import forms

class Create_new_task(forms.Form):
    title = forms.CharField(label="Titulo de la tarea", max_length=200, required=False, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label="Descripcion de la tarea", max_length=400, required=False, widget=forms.Textarea(attrs={'class':'input'}))

class Create_new_project(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200, required=False, widget=forms.TextInput(attrs={'class':'input'}))