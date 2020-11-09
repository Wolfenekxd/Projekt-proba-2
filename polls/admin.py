from django.contrib import admin
from .models import polls,voted,single_answers
# Register your models here.

admin.site.register(polls)
admin.site.register(voted)
admin.site.register(single_answers)