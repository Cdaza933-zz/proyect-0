from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from events.forms import EventForm
from events.models import Event, Category


def event_list(request):
    events_list = Event.objects.filter(host=request.user).order_by('-pk')
    context = {"events_list": events_list}
    return render(request, 'events/event_list.html', context)


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        event_data = form.data.dict()
        event_data.pop('csrfmiddlewaretoken')
        category = Category.objects.get(pk=event_data.pop('category'))
        Event.objects.create(host=request.user, category=category, **event_data)
        return HttpResponseRedirect(reverse('event_list'))
    form = EventForm()
    return render(request, 'events/add.html', {'form': form})


def delete_event(request, event_id):
    if request.method == 'DELETE':
        Event.objects.get(pk=event_id).delete()
        events_list = Event.objects.filter(host=request.user).order_by('-pk')
        context = {"events_list": events_list}
        return render(request, 'events/event_list.html', context)
    return HttpResponseRedirect(reverse('event_list'))


def edit_event(request, event_id):
    if request.method == 'POST':
        form = EventForm(request.POST)
        event_data = form.data.dict()
        event_data.pop('csrfmiddlewaretoken')
        category = Category.objects.get(pk=event_data.pop('category'))
        Event.objects.filter(pk=event_id).update(**event_data, category=category)
        events_list = Event.objects.filter(host=request.user).order_by('-pk')
        return HttpResponseRedirect(reverse('event_list'))
    event = Event.objects.get(pk=event_id)
    form = EventForm(event.__dict__)
    return render(request, 'events/edit.html', {'form': form, 'event_id': event_id})