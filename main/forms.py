from django import forms


class LinkBookMark2(forms.Form):
    url = forms.URLField(label='Add Link', max_length=255)


class LinkBookMark(forms.Form):
    attrs = {
        'id' : "inlineFormInputName2",
        'placeholder' : "URL",
        'class': 'form-control is-valid'
    }
    url = forms.URLField(label='Add Link', max_length=255, widget=forms.TextInput(attrs=attrs))
