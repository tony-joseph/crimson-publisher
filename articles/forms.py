from django.forms import ModelForm, TextInput, Textarea, EmailInput

from articles.models import Comment


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }
