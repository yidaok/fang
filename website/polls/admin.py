from django.contrib import admin
from .models import Question,Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                    (None,               {'fields': ['question_text']}),
                    ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
                ]
    inlines = [ChoiceInLine]
    list_display = ['question_text','pub_date']

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text','votes']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
# Register your models here.
