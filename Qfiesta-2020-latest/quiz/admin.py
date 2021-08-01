from django.contrib import admin
from .models import Profile,Question, Image, Audio, Video

# Register your models here.
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Image)
admin.site.register(Audio)
admin.site.register(Video)