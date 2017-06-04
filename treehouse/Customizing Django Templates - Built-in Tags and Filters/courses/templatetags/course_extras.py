from django import template

from courses.models import Course


register = template.Library()

@register.simple_tag
def newest_course():
    """ Gets the most recent course that was added to the library. """
    return Course.objects.latest('created_at')

# register.simple_tag('newest_course') (longer way of the @ version above)

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    """ Returns dictionary of courses to display as navigation pane """
    courses = Course.objects.all()
    return {'courses': courses}

# register.inclusion_tag('courses/course_nav.html')(nav_courses_list)