from rest_framework import serializers
from .models import VideoMem


class VidMemSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoMem
        fields = ["video_name", "video", "caption"]
