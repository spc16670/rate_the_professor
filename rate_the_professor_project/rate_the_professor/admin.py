from django.contrib import admin
from rate_the_professor.models import Admin, UserProfile, Rating, University, Course, Professor, Department, Suggestion


# Just pass for now
class PageAdmin(admin.ModelAdmin):
    pass


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('full_name','university', 'courses_taught','date_added')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('university','department_name')

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'university', 'no_of_ratings', 'overall_rating')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','university','department','start_date')

# Register models
admin.site.register(Admin, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Rating)
admin.site.register(University)
admin.site.register(Course, CourseAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Suggestion, SuggestionAdmin)