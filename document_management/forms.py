from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            file_name = file.name
            if not file_name.endswith('.pdf') and not file_name.endswith('.docx'):
                raise forms.ValidationError('Only PDF and DOCX files are allowed.')
        return file
