from django.db import models
from app.models import Course

class Video(models.Model):
    tittle = models.CharField(max_length=30, null = True)
    course = models.ForeignKey(Course,null=True,on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=True)
    video_url = models.CharField(max_length=200, null = True)
    is_preview = models.BooleanField(default=0)

    def __str__(self):
        return self.tittle
