from django.contrib import admin

# Register your models here.

from polls.models import Question, Choice


""" 

field order
class QuestionAdmin(admin.ModelAdmin):
     fields = ['pub_date', 'question_text']

"""



# StackedInline
"""
class ChoiceInline(admin.StackedInline):
     model = Choice
     extra = 2
"""

# TabularInline
class ChoiceInline(admin.TabularInline):
     model = Choice
     extra = 2

# field separation and collapse 
class QuestionAdmin(admin.ModelAdmin):
     fieldsets = [
          ('Question Statement', {'fields': ['question_text']}),
          ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
     ]
     inlines = [ChoiceInline]  # Choice model class under Question model
     list_display = ('question_text', 'pub_date')  # list column created

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)




