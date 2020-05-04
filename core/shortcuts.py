from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import resolve_url


def redirect(to, *args, permanent=False, **kwargs):
    redirect_class = (
        HttpResponsePermanentRedirect if permanent else HttpResponseRedirect
    )
    url = resolve_url(to, *args, **kwargs)
    response = redirect_class(url)
    response["Trubolinks-Location"] = url
    return response
