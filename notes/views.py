from django.shortcuts import render

# Create your views here.
from .models import Notes

def list(request):
    allnotes = Notes.objects.all()
    return render(request,'notes/notes_list.html',{'notes': allnotes})