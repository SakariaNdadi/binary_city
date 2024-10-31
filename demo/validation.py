from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import models


def check_client_name(request):
    name = request.POST.get("name")
    if models.Client.objects.filter(name=name).exists():
        return HttpResponse(
            "<p class='text-red-500 text-sm mt-1'>Client name already exists</p>"
        )
    else:
        return HttpResponse(
            "<p class='text-green-800 text-sm mt-1'>Client name available</p>"
        )
