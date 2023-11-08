from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='is_teacher')
def is_teacher(user):
    try:
        teacher_group = Group.objects.get(name='Teacher')
        return teacher_group in user.groups.all()
    except Group.DoesNotExist:
        return False
@register.filter(name='is_student')
def is_student(user):
    try:
        student_group = Group.objects.get(name='Student')
        return student_group in user.groups.all()
    except Group.DoesNotExist:
        return False