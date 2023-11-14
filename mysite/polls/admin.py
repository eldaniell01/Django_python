from django.contrib import admin
from .models    import Choice, Question

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ('PREGUNTA', {'fields': ['question_text']}),
        ('FECHA', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
