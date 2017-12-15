from django import forms


class LinkBookMark(forms.Form):
    url = forms.URLField(label='Add Link', max_length=255)