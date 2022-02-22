from django.shortcuts import render

def index_view(request):
    msg = "hello world"

    context = {
        "msg": msg
        }
    return render(request, "index.html", context)
