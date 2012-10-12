from django import template

from lessons.models import Lesson

register = template.Library()


@register.assignment_tag
def all_lessons():
    return Lesson.objects.all()
