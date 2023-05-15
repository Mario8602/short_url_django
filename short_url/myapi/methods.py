from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Token


def get_full_url(url):
    try:
        token = Token.objects.get(short_url=url)
        if not token.is_active:
            raise KeyError('Token is not active')
    except Token.DoesNotExist:
        raise KeyError('Url does not exist')
    
    token.number_transitions += 1
    token.save()

    return token.full_url


def redirection(request, short_url):
    try:
        full_url = get_full_url(short_url)
        return redirect(full_url)
    except Exception as ex:
        return HttpResponse(ex.args)