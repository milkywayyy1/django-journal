from django import template

from people.models import Teacher, User


register = template.Library()


@register.inclusion_tag('people/tpl/student_sidebar_tpl.html', name='student_sidebar')
def student_sidebar(user):
    group_student = User.objects.select_related('student__group').get(pk=user.face_id)
    user_group_manager = User.objects.select_related('teacher')\
        .get(teacher__group_manager=group_student.student.group_id)
    return {'user': user, 'user_group_manager': user_group_manager}


@register.inclusion_tag('people/tpl/teacher_sidebar_tpl.html', name='teacher_sidebar')
def teacher_sidebar(user):
    teacher = Teacher.objects.get(user=user.face_id)
    return {'teacher': teacher, 'user': user}

