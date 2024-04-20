from django.contrib import admin
from .models import Instructor, Skill, Course, Module, Lesson, Enrollment



class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'duration_weeks', 'instructor', 'about', 'skills_list')
    list_filter = ('start_date', 'skills')
    search_fields = ('title', 'description', 'about')
    list_editable = ('duration_weeks', 'instructor')  # Removed 'start_date' from list_editable

    def skills_list(self, obj):
        # Display skills as a list of <li> elements in the admin list view
        return '<ul>{}</ul>'.format(''.join(f'<li>{skill}</li>' for skill in obj.skills.all()))

    skills_list.short_description = 'Skills'  # Custom column header name for skills







@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'contact_info')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'lesson_type')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'enrollment_date')  # Updated to use 'name' instead of 'user'

# Remove these lines as they are redundant
# admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
# admin.site.register(Module, ModuleAdmin)
# admin.site.register(Lesson, LessonAdmin)
# admin.site.register(Enrollment, EnrollmentAdmin)
