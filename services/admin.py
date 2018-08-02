from django.contrib import admin

from .models import (
    Sentence,
    Text,
    Word,
    State,
    Structure,
)

admin.site.register(Sentence)
admin.site.register(Text)
admin.site.register(Word)
admin.site.register(State)
admin.site.register(Structure)
