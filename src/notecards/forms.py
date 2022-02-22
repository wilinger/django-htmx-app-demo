from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
from django import forms
from .models import Notecard

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notecard
        fields = ['title', 'content']

    title = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '50',}))   
    def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(NoteForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
                Div(
                    Field('title', wrapper_class="col-sm-12"),
                    css_class='row',
                ),
                Div(
                    Field('content', wrapper_class="col-sm-12"),
                    css_class='row',
                )
            )
