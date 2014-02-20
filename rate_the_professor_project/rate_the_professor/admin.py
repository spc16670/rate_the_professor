from django.contrib import admin
from rate_the_professor.models import Admin, UserProfile, Rating, University, Course, Lecturer

# Just pass for now
class PageAdmin(admin.ModelAdmin):
    pass

# Register models
admin.site.register(Admin, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Rating)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(Lecturer)