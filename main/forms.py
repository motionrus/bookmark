from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class LinkBookMark(forms.Form):
    attr = {
        'id': "inlineFormInputName2",
        'placeholder': "URL",
        'class': 'form-control is-valid'
    }
    url = forms.URLField(
        label='Add Link', max_length=255,
        widget=forms.TextInput(attrs=attr)
    )


class SearchForm(forms.Form):
    search_parameters = forms.CharField(
        label='Search',
        max_length=100
    )


class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(500)
        ]
    )
