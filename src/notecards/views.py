from django.views.generic import ListView, DetailView
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from notecards.models import Notecard
from .forms import NoteForm


def index(request):
    return render(request, 'notecards/index.html')

class NotecardListView(ListView):
    model = Notecard
    template_name = 'notecards/partials/notecard_list.html'

class NotecardDetailView(DetailView):
    model = Notecard
    template_name = 'notecards/partials/notecard_detail.html'

def notecard_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'update_notecard_list'})
    else:
        form = NoteForm()

    template_name = 'notecards/partials/notecard_form.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)

def notecard_update(request, pk):
    notecard = get_object_or_404(Notecard, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=notecard)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'update_card_list'})
    else:
        form = NoteForm(instance=notecard)
    template_name = 'notecards/partials/notecard_form.html'
    context = {
        'form': form,
        'notecard': notecard
    }
    return render(request, template_name, context)

def notecard_delete(request, pk):
    if request.method == "DELETE":
        notecard = get_object_or_404(Notecard, pk=pk)
        notecard.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'update_notecard_list'})
    else:
        return HttpResponseBadRequest("Invalid request")