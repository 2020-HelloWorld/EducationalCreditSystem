from django.contrib import admin
from .models import event,participant,organizer,winner,image

# Register your models here.
admin.site.register(event)
admin.site.register(participant)
admin.site.register(organizer)
admin.site.register(winner)
admin.site.register(image)
