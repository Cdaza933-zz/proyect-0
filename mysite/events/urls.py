from django.conf.urls import url
from django.urls import path

from events.views import event_list, add_event, delete_event, edit_event

urlpatterns = [
    # url(r'^event/(?P<city_id>\d+)/$', EventDetailViewSet.as_view(), name='event manager'),
    url(r'^add', add_event, name='add_event'),
    url(r'^$', event_list, name='event_list'),
    url(r'^(?P<event_id>[0-9]+)/delete$', delete_event, name='delete_event'),
    url(r'^(?P<event_id>[0-9]+)$', edit_event, name='edit_event'),
]