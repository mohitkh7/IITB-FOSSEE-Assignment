from django.contrib import admin

from .models import User, Foss, TutorialDetail, Payment

# Register your models here.
admin.site.register(User)
admin.site.register(Foss)
admin.site.register(TutorialDetail)
admin.site.register(Payment)
