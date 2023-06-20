from django.db import models

# Create your models here.


class VideoMem(models.Model):
    video_name = models.CharField(max_length=100)
    video = models.FileField()
    caption = models.TextField()
    score = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.video_name