from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from django.contrib import admin
from .models import Home

#Enter New Code
#Basically, add the 'Home' class to the admin page so that it can be edited with correct formatting and django tools and also registers it correctly
#Furthermore, add function so to see previously editted boxes and their history
#at the admin page, give option to 'edit home' instead of 'add homes'
#I want to add a button that basically deletes the previous saved HomeAdmin



class HomeAdmin(admin.ModelAdmin):
    list_display = ('about', 'research', 'events')  # Display these fields in the admin list view
    list_filter = ['about', 'research', 'events']  # Add filtering options
    search_fields = ['about', 'research', 'events']  # Add search functionality

admin.site.register(Home, HomeAdmin)  # Register the Home model with the HomeAd

'''
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('syllabus', 'experiments', 'sidebars')
    list_filter = ['syllabus', 'experiments', 'sidebars']
    search_fields = ['syllabus', 'experiments', 'sidebars']
admin.site.register(Syllabus, SyllabusAdmin)

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('person', 'image')
    list_filter = ['person', 'image']
    search_fields = ['person', 'image']
admin.site.register(People, PeopleAdmin)
'''


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)