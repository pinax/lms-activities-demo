from django.contrib import admin

from .models import Vocabulary


admin.site.register(Vocabulary, list_display=["word", "definition"])
