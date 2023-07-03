from django.contrib import admin

# Register your models here.

from polls.models import Question, Choice

# field order 
class QuestionAdmin(admin.ModelAdmin):
     fields = ['pub_date', 'question_text']

admin.site.register(Question)
admin.site.register(Choice)


