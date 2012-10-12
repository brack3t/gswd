from django import template

from lessons.models import Lesson, Translation

register = template.Library()


@register.assignment_tag
def all_lessons():
    return Lesson.objects.all()


@register.assignment_tag
def get_translation(lesson, language):
    return Translation.objects.get(lesson_id=lesson.pk, language=language)
