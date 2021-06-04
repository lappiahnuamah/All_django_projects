from django import forms
from django.db import models
from django.db.models import fields
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows':'4',
    }))

    class Meta:
        model = Comment
        fields = ('content',)