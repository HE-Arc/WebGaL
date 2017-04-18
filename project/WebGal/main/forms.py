from django import forms
from multiupload.fields import MultiFileField


class UploadProject(forms.Form):
    project_name = forms.CharField(label='Project Name', max_length=100)
    description = forms.CharField(label='Description', max_length=4000, widget=forms.Textarea)
    image = forms.ImageField(label='Thumbnail')
    attachments = MultiFileField(label='Project Files', min_num=1)


class AddComment(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
