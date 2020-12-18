import asyncio

from django.http.response import JsonResponse
from django.shortcuts import render
from asgiref.sync import sync_to_async

from .models import FilteredValues


def filter_unique(ip):
    d = {}
    for i in ip:
        try:
            d[i] = d[i]+1
        except KeyError:
            d[i] = 1
    l = [k for (k, v) in d.items() if d[k] == 1]
    return l


async def store_computed_values(inputs, output):
    FilteredValues.objects.create(inputs=inputs, output=output)


def filter_view(request):
    ip = request.GET.get('values')
    elements = ip.split(',')
    if ip:
        output = filter_unique(elements)
        asyncio.run(store_computed_values(ip, ','.join(output)))
        return JsonResponse({"data": output})
    return JsonResponse({"error": "atleast one value is required"}, status=400)
