from django import forms

from .models import Token


# class TokenForm(forms.ModelForm):

#     full_url = forms.URLField()
#     short_url = forms.CharField(max_length=6, required=True)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if not self.instance.pk:
#             self.fields['short_url'].initial = self.instance.gen_token()

#     class Meta:
#         model = Token
#         exclude = ('short_url', 'number_transitions')

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.short_url = instance.gen_token()
#         if commit:
#             instance.save()
#         return instance

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