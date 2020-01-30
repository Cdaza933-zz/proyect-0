from bootstrap_datepicker_plus import DateTimePickerInput
from django.forms import ModelForm, DateTimeField
from events.models import Event


class EventForm(ModelForm):
    end_date = DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=DateTimePickerInput(format='%Y-%m-%d %H:%M')
    )
    beginning_date = DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=DateTimePickerInput(format='%Y-%m-%d %H:%M'),
    )

    class Meta:
        model = Event
        fields = ('id', 'name', 'category', 'address', 'place', 'beginning_date', 'end_date', 'image')
