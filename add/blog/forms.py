from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'image', 'body',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Напишите ваш комментарий'})
        }
