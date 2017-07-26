from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from events.models import events
from django.views import generic
# Create your views here.

class indexview(generic.ListView):
	template_name='events.html'
	context_object_name='allEvent'
	def get_queryset(self):
		return events.objects.all()
class Detailview(generic.DetailView):
	model=events
	template_name='events.html'