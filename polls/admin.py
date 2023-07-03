from django.contrib import admin

# Register your models here.

from polls.models import Question, Choice


""" 

field order
class QuestionAdmin(admin.ModelAdmin):
     fields = ['pub_date', 'question_text']

"""
# field separation and collapse 

class QuestionAdmin(admin.ModelAdmin):
     fieldsets = [
          ('Question Statement', {'fields': ['question_text']}),
          ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
     ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


