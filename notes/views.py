from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView,  DetailView, ListView , UpdateView
from .models import Notes
from .forms import NotesForm
from django.views.generic.edit import DeleteView

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'

    
class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
    model = Notes
    template_name= 'notes/notes_detail.html'
    context_object_name = 'note'



def detail(request,pk):
    try:
       note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request,'notes/notes_detail.html', {'note': note})