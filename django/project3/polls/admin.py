# coding: utf-8

from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline): # admin.StackedInline stack형태로 보여줌 
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None , {'fields': ['question_text']}),
            ('Date Information', {'fields': ['pub_date']}),
    ] # 각 레코드 생성, 수정시 화면 제어 
    inlines = [ChoiceInline] # 외래키 설정된 항목들을 테이블 형식으로 보여줌
    list_display = ('question_text', 'pub_date') # admin페이지에서 레코드 리스트의 칼럼 추가
    list_filter = ['pub_date'] # 핉터 사이드 바 추가 
    search_fields = ['question_text'] # 검색 박스 추가 

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

