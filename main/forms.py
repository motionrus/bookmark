from django import forms


class LinkBookMark(forms.Form):
    attr = {
        'id': "inlineFormInputName2",
        'placeholder': "URL",
        'class': 'form-control is-valid'
    }
    url = forms.URLField(label='Add Link', max_length=255, widget=forms.TextInput(attrs=attr))
