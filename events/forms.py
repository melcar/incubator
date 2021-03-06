from django.forms import ModelForm, Textarea
from datetimewidget.widgets import DateTimeWidget

from django import forms

from .models import Event, Meeting


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

        widgets = {
            'start': DateTimeWidget(
                attrs={'id': "start"},
                usel10n=True,
                bootstrap_version=3
            ),
            'stop': DateTimeWidget(
                attrs={'id': "stop"},
                usel10n=True,
                bootstrap_version=3
            ),
            'description': Textarea(attrs={'rows': 15}),
        }

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        start = cleaned_data.get("start")
        stop = cleaned_data.get("stop")
        status = cleaned_data.get("status")

        if start and stop:
            if stop < start:
                raise forms.ValidationError(
                    "La date de fin ne peut être avant la date de début"
                )

        if (not stop) and start:
            cleaned_data['stop'] = start

        if status == "r" and not start:
            raise forms.ValidationError(
                "Un événement prêt doit avoir une date de début"
            )


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ('OJ', 'PV')
