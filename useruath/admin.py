from django.contrib import admin

# Register your models here.
from .models import User,questions

admin.site.register(User)
admin.site.register(questions)