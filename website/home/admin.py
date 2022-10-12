
from django.contrib import admin

from home.models import Contact, Event, Gallery, PostBearer, Announcement, carousel

# Register your models here.

admin.site.register(Contact)
admin.site.register(PostBearer)
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(Announcement)
admin.site.register(carousel)