from django.contrib import admin
from app.models import Course, Tag, Prerequisite, Learning, Video

# Register your models here.
class TagAdmin(admin.TabularInline):
    model = Tag
    extra = 1
    
class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite
    extra = 1
    
class LearningAdmin(admin.TabularInline):
    model = Learning
    extra = 1
    
class VideoAdmin(admin.TabularInline):
    model = Video
    extra = 1
    
class CourseAdmin(admin.ModelAdmin):
    inlines = [PrerequisiteAdmin,LearningAdmin,TagAdmin,VideoAdmin]
admin.site.register(Course,CourseAdmin)
# admin.site.register(Tag)
# admin.site.register(Prerequisite)   instead of this we will inline all this tags and description inside the course model while registring the course
# admin.site.register(Learning)


