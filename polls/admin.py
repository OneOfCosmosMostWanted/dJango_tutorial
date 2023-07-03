from django.contrib import admin

# Register your models here.

from polls.models import Question, Choice


""" 

field order
class QuestionAdmin(admin.ModelAdmin):
     fields = ['pub_date', 'question_text']

"""
# field separation

class QuestionAdmin(admin.ModelAdmin):
     fieldsets = [
          ('Question Statement', {'fields': ['question_text']}),
          ('Date Information', {'fields': ['pub_date']}),
     ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


