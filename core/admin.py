from django.contrib import admin
from .forms import PersonCreateForm
from .models import *

class PersonCreateAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'gender', 'phone', 'ip', 'adress']
    form = PersonCreateForm
    list_filter = ['name', 'email', 'gender', 'phone', 'ip', 'adress']
    search_fields = ['name', 'email', 'gender', 'phone', 'ip', 'adress']

# Register your models here.
admin.site.register(Person, PersonCreateAdmin)