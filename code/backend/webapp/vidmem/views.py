from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import VideoMem
from .serializers import VidMemSerializer
from ml_backend.video_preprocessing import preprocess_video
from ml_backend.trained_models import time_distributed_lstm_model

# Create your views here.

class ListCreateVidMem(ListCreateAPIView):
    queryset = VideoMem.objects.all()
    serializer_class = VidMemSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = VidMemSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        processed_video = preprocess_video(obj.video.path)
        mem_score = time_distributed_lstm_model(processed_video)
        print(mem_score)
        return Response({"mem_score": mem_score}, status=status.HTTP_200_OK)


def index(request):
    return render(request, "index.html")