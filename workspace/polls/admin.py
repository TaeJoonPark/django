from django.contrib import admin
from polls.models import Question, Contact, Choice

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Contact)


list_display = ('name', 'nowDate')
list_filter = ['nowDate']

# Register your models here.
