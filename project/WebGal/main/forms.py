from django import forms


class FileFieldForm(forms.Form):
    project_name = forms.CharField(max_length=254,
                                   widget=forms.TextInput(attrs={'autofocus': ''}),
                                   label="Project Name")
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
