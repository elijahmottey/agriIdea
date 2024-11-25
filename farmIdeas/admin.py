from django.contrib import admin
from .models import ContactUs,Idea,Comment


# Register your models here.
admin.site.register(ContactUs)
admin.site.register(Idea)
admin.site.register(Comment)
