from django import forms


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


class Search_Form(forms.Form):
    search_parameters = forms.CharField(
        label='SearcH',
        max_length=100
    )

# https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(500)
        ]
    )