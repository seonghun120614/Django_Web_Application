from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline) : # Tabular 형태로 보여주기
    model = Choice  # 보여줄 모델 설정
    extra = 3       # 몇 개 보여줄지 개수 설정


class QuestionAdmin(admin.ModelAdmin) :
    fieldsets = [
        (
            None,
            {
                'fields': ['question_text'],
            }
        ),
        (
            'Date information', 
            {
                'fields': ['pub_date'],
                'classes': ['collapse'],
            }
        ),
    ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


# admin 사이트에 Question을 추가하고,
# QuestionAdmin을 추가함
admin.site.register(Question, QuestionAdmin)