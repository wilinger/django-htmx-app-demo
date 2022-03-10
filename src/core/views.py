from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index_view(request):
    msg = "Welcome to the Notecards app."

    context = {"msg": msg}
    return render(request, "index.html", context)
