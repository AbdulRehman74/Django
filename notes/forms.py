from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')


def clean_title(self):
    title = self.cleaned_data['title']
    if 'Django' not in title:
        raise forms.ValidationError('we only accept notes with Django ')
    return title