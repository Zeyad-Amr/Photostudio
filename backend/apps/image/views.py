from rest_framework.response import Response
from rest_framework import viewsets
from image.models import Image
from api.serializer import *


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    # create image obj then save it and return the image url in the response
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def list(self, request):
        queryset = Image.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
