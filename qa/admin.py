from django.contrib import admin

from qa.models import Answer, AnswerComment, Question


admin.site.register(Answer)
admin.site.register(AnswerComment)
admin.site.register(Question)
