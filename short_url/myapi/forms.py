from django import forms

from .models import Token


class TokenForm(forms.ModelForm):

    full_url = forms.URLField()

    class Meta:
        model = Token
        exclude = ('number_transitions',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.instance.short_url = self.instance.gen_token()
            self.initial['short_url'] = self.instance.short_url
