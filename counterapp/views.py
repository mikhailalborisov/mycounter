import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views her

value = 1


def counter(request):
    global value

    try:
        if request.method == "POST":
            value = json.loads(request.body)["value"]
        return JsonResponse({"count": value})
    except:
        return JsonResponse({"count": "400"})


def increment(request):
    global value
    try:
        value = value + json.loads(request.body)["diff"]
        return JsonResponse({"count": value})
    except:
        return JsonResponse({"count": "400"})


def decrement(request):
    global value
    try:
        value = value - json.loads(request.body)["diff"]
        return JsonResponse({"count": value})
    except:
        return JsonResponse({"count": "400"})
