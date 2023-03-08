from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core.files import File
from image.models import Image
from processing.Histograms import Histograms
from .serializer import ImageSerializer,ImageSerializerArr
import numpy as np
import cv2


# @api_view(['GET'])
# def get(request):
#     body = {"fads": "fasffds"}
#     return Response(body)

IMAGES_FOLDER = './mediaFiles/'


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
            return Response(data=serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        image = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(image)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], url_path=r'process')
    def process(self, request, pk=None):
        image = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(image)
        imgPath = IMAGES_FOLDER+serializer.data.get("image")
        print(imgPath)
        imageArr = cv2.imread(imgPath, 0)
        file_name = serializer.data.get("image").split("/")[2]
        option = request.data.get('option')
        isSaved = False
        if(option == '1'):
            imgOperator = Histograms(imageArr)
            print(serializer)
            newImg = imgOperator.applyGlobalThreshold(50)
            
            serializerRes = ImageSerializerArr(data={"image": newImg})
            if serializerRes.is_valid():
                serializerRes.save()
                print(serializerRes.data.get("image"))
                return Response(data=serializerRes.data, status=200)
            else:
                return Response(serializerRes.errors, status=400)
            # print(serializer.data.get("image").split("/")[2])
            # result_path = IMAGES_FOLDER + 'result/' + file_name
            # print(result_path)
            # isSaved = cv2.imwrite(result_path, newImg)

        return Response({"msg": "Please provide valid option"}, status=500)
