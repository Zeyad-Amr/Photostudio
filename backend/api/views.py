from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from image.models import Image
from processing.Histograms import Histograms
from .serializer import ImageSerializer
import numpy
import cv2


@api_view(['GET'])
def get(request):
    body = {"fads": "fasffds"}
    return Response(body)


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    def create(self, request):
        # typee = request.data['type']
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data.get("image"))
            imgPath = './mediaFiles/'+serializer.data.get("image")
            imageArr = cv2.imread(imgPath, 0)
            imgOperator = Histograms(imageArr)
            newImg = imgOperator.applyGlobalThreshold(50)
            cv2.imwrite(imgPath, newImg)

            # print(imageArr)
            return Response(data={"msg": serializer.data}, status=200)
        else:
            return Response(serializer.errors, status=400)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        image = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(image)
        return Response(serializer.data)
