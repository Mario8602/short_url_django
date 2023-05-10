from django import forms

from .models import Token


class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        exclude = ('short_url', 'number_transitions')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.short_url = instance.gen_token()
        if commit:
            instance.save()
        return instance
