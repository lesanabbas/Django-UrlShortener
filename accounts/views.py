import os
from django.shortcuts import render
from dotenv import load_dotenv
from django.http import HttpResponseRedirect

load_dotenv()


def indexView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        return render(request, "accounts/index.html", {'BASE_URL': "https://snaplinks.vercel.app"})
