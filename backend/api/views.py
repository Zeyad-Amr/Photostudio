import random
import string
from matplotlib import pyplot as plt
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core.files import File
from image.models import Image
from processing.Histograms import Histograms
from .serializer import ImageSerializer, ImageSerializerArr
import numpy as np
import cv2
import matplotlib
matplotlib.use('Agg')


IMAGES_FOLDER = './mediaFiles/'



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


    # the api that process second tab (histograms) functions
    @action(detail=True, methods=["post"], url_path=r'process')
    def process(self, request, pk=None):
        # get the image given its id (pk = primary key)
        image = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(image)
        # get the image path to read it w/ cv2 and pass it to Histogram class
        imgPath = IMAGES_FOLDER+serializer.data.get("image")
        imageArr = cv2.imread(imgPath, 0)
        imgOperator = Histograms(imageArr)

        # get the request data 
        option = request.data.get('option')
        globalThreshold = request.data.get('globalThreshold')
        blocksize = request.data.get('blocksize')
        c = request.data.get('c')

        # random name to prevent histogram or cumulative images from overwriting
        randomName = ''.join(random.choices(string.ascii_letters, k=3))


        if(option == '1'):
            operatedImg = imgOperator.equalize()
            self._drawHistAndCum(imgOperator, operatedImg, randomName)
        elif(option == '2'):
            operatedImg = imgOperator.normalise()
            self._drawHistAndCum(imgOperator, operatedImg, randomName)
        elif(option == '3' and blocksize != None and c != None):
            operatedImg = imgOperator.applyLocalThreshold(blocksize,c)
            self._drawHistAndCum(imgOperator, operatedImg, randomName)
        elif(option == '4' and globalThreshold != None):
            operatedImg = imgOperator.applyGlobalThreshold(globalThreshold)
            self._drawHistAndCum(imgOperator, operatedImg, randomName)
        else:
            return Response({"histURL": "", "cumURL": "", "image": ""}, status=200)

        # create the output image
        serializerRes = ImageSerializerArr(data={"image": operatedImg})
        if serializerRes.is_valid():
            serializerRes.save()
            return Response(data={**serializerRes.data,
                                  **{"histURL": "http://127.0.0.1:8000/result/histogram" + randomName + ".jpg",
                                     "cumURL": "http://127.0.0.1:8000/result/cumulative" + randomName + ".jpg"}},
                            status=200)
        else:
            return Response(serializerRes.errors, status=400)



    def _drawHistAndCum(self, imgOperator, img, pk):
        hist = imgOperator.getHistoGram(img)
        plt.hist(imgOperator.flatten(img))
        plt.savefig(IMAGES_FOLDER + "/result/histogram" + pk + ".jpg")
        plt.clf()
        plt.plot(imgOperator.getCumSum(hist))
        plt.savefig(IMAGES_FOLDER + "/result/cumulative" + pk + ".jpg")
        plt.close()
