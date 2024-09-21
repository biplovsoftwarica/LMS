# we can't create the dependent entitis directly
#so first we would need to create indipentdent entity
# here independent entity is course entity
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30, null = False)
    description = models.CharField(max_length=300, null = True)
    price = models.IntegerField(null=False, default=0)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=0)
    thumbnail = models.ImageField(upload_to="files/thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to="files/resource")
    course_length = models.IntegerField(null=False, default=1)
    def __str__(self):
        return self.name
    
class Course_property(models.Model):
    description = models.CharField(max_length=20,null=True)
    course = models.ForeignKey(Course,null=True,on_delete=models.CASCADE)
    class Meta:
        abstract = True
        # what this does is create models for all those three but not for course property
    
class Tag(Course_property):
    pass
    
class Prerequisite(Course_property):
    pass
    
class Learning(Course_property):
    pass