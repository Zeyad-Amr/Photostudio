from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from image.models import Image
from .serializer import ImageSerializer


@api_view(['GET'])
def get(request):
    body = {"fads": "fasffds"}
    return Response(body)


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    def create(self, request):
        print(request.data)
        type = request.data['type']
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(data={"msg": serializer.data, "type": type}, status=200)
        else:
            return Response(serializer.errors, status=400)
        
        
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        image = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(image)
        return Response(serializer.data)

