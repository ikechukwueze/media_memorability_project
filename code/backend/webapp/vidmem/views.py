from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import VideoMem
from .serializers import VidMemSerializer
from ml_backend.trained_models import predict_mem_score

# Create your views here.

class ListCreateVidMem(ListCreateAPIView):
    queryset = VideoMem.objects.all()
    serializer_class = VidMemSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = VidMemSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        mem_score = predict_mem_score(obj.video.path, obj.caption)
        return Response({"mem_score": mem_score}, status=status.HTTP_200_OK)


def index(request):
    return render(request, "index.html")