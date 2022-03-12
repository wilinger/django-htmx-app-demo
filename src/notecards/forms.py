from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout
from django import forms
from django.core.exceptions import ValidationError

from core.settings import MAX_RECORDS

from .models import Notecard


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notecard
        fields = ["title", "content"]

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "maxlength": "50",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(NoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field("title", wrapper_class="col-sm-12"),
                css_class="row",
            ),
            Div(
                Field("content", wrapper_class="col-sm-12"),
                css_class="row",
            ),
        )

    def clean(self):
        cleaned_data = super(NoteForm, self).clean()
        title = cleaned_data.get("title")
        if (
            not Notecard.objects.filter(title=title).exists()
            and Notecard.objects.count() >= MAX_RECORDS
        ):
            raise ValidationError(
                f"Maximum limit of {MAX_RECORDS} notecards reached. Please delete a notecard."
            )
        return cleaned_data
