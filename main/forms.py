from django import forms


class LinkBookMark(forms.Form):
    url = forms.URLField(label='Link', max_length=255)
    print(url)