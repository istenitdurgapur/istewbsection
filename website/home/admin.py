
from django.contrib import admin

from home.models import Contact, Event, Gallery, PostBearer

# Register your models here.

admin.site.register(Contact)
admin.site.register(PostBearer)
admin.site.register(Event)
admin.site.register(Gallery)