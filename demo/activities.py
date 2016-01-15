from django import forms

from pinax.lms.activities.base import Survey


class SuggestionBox(Survey):

    title = "Suggestion Box"
    description = "make a suggestion on how to improve the site"

    repeatable = True

    questions = [
        {
            "name": "suggestion",
            "label": "Suggestion",
            "field_class": forms.CharField,
            "extra_args": {
                "widget": forms.Textarea(attrs={"rows": "5", "class": "col-md-8"}),
            }
        }
    ]
