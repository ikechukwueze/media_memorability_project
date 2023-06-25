from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import VideoMem
from .serializers import VidMemSerializer

# Create your views here.

class ListCreateVidMem(ListCreateAPIView):
    queryset = VideoMem.objects.all()
    serializer_class = VidMemSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = VidMemSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        import time
        time.sleep(1)
        resp = {"score":100}
        return Response(resp, status=status.HTTP_200_OK)

    # def post(self, request, *args, **kwargs):
    #     video_file = request.FILES['file_field_name']
    # filename = '/tmp/myfile'
    # with open(filename, 'wb+') as temp_file:
    #     for chunk in my_file.chunks():
    #         temp_file.write(chunk)

    # my_saved_file = open(filename) #there you go
    #     return super().post(request, *args, **kwargs)


def index(request):
    return render(request, "index.html")