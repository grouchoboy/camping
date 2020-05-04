from django.forms import ModelForm
from django import forms

from .models import Project, Message


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("name", "description")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "input input--full-width",
                    "placeholder": "e.g. Office Renovation",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "input input--full-width",
                    "rows": "3",
                    "placeholder": "e.g. Plans and scheduling for expanding the office",
                }
            ),
        }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ("title", "content", "project")
        widgets = {
            "project": forms.HiddenInput,
            "title": forms.TextInput(
                attrs={
                    "class": "input input--full-width input--borderless input--header",
                    "placeholder": "Type a title...",
                }
            ),
            "content": forms.HiddenInput(
                attrs={
                    "class": "input input--full-width",
                    "placeholder": "Write away...",
                }
            ),
        }
