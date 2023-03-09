from .models import Spice, Comment, TypeCategory
from django import forms
from django.forms import fields, ModelForm


class AddSpice(forms.ModelForm):

    class Meta:
        model = Spice
        fields = ('image', 'name', 'description', 'use_category',
                  'type_category', 'price', 'bookmark', )
        prepopulated_fields = {'slug': 'name', }


class SearchCategory(forms.ModelForm):
    class Meta:
        model = Spice
        fields = ('use_category',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
