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
from processing.Frequency import Frequency
from .serializer import *
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

    def list(self, request):
        queryset = Image.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["delete"], url_path=r'delete')
    def delete_all(self, request):
        instance = Image.objects.all()
        instance.delete()
        # you custom logic #
        return Response(instance)

    # the api that process second tab (histograms) functions

    @action(detail=True, methods=["post"], url_path=r'histograms_process')
    def histoProcess(self, request, pk=None):
        # get the image given its id (pk = primary key)
        image = get_object_or_404(self.queryset, pk=pk)
        # get the image path to read it w/ cv2 and pass it to Histogram class
        imageArr = self._readImage(image)
        imgOperator = Histograms(imageArr)

        # get the request data
        option = request.data.get('option')
        globalThreshold = request.data.get('globalThreshold')
        blocksize = request.data.get('blocksize')
        c = request.data.get('c')

        # random name to prevent histogram or cumulative images from overwriting
        randomName = ''.join(random.choices(string.ascii_letters, k=3)) + pk

        if(option == '1'):
            operatedImg = imgOperator.equalize()
            self._drawHistAndCum(imgOperator, operatedImg, randomName)
        elif(option == '2'):
            operatedImg = imgOperator.normalise()
            self._drawHistAndCum(imgOperator, operatedImg, randomName)
        elif(option == '3' and blocksize != None and c != None):
            operatedImg = imgOperator.applyLocalThreshold(blocksize, c)
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
                                  **{"histURL": "http://127.0.0.1:8000/result/hist" + randomName + ".jpg",
                                     "cumURL": "http://127.0.0.1:8000/result/cum" + randomName + ".jpg"}},
                            status=200)
        else:
            return Response(serializerRes.errors, status=400)

    # the api that process third tab (frequancy) functions

    @action(detail=False, methods=["post"], url_path=r'frequancy_process')
    def freqProcess(self, request):
        # get the image given its id (pk = primary key)
        f_imgId = request.data.get("f_imgId")
        s_imgId = request.data.get("s_imgId")
        image1 = get_object_or_404(self.queryset, pk=f_imgId)
        image2 = get_object_or_404(self.queryset, pk=s_imgId)
        # read the image to 2d array
        imageArr1 = self._readImage(image1, 1)
        imageArr2 = self._readImage(image2, 1)

        # get cuttof frequancies
        # lowCutoff = request.data.get("lowCutoff")
        # highCutoff = request.data.get("highCutoff")
        lowCutoff = 0
        highCutoff = 0

        option = request.data.get("option")

        if(option == '1'):
            L_image = imageArr2
            H_image = imageArr1
        elif(option == '2'):
            L_image = imageArr1
            H_image = imageArr2
        else:
            return Response(data={"image": ""})

        imgOperator = Frequency()
        lowPass = imgOperator.low_pass_filter(L_image, lowCutoff)
        highPass = imgOperator.high_pass_filter(H_image, highCutoff)

        hybrid = imgOperator.hypridImages(lowPass, highPass)
        serializerRes = ImageSerializerArr(data={"image": hybrid})
        if serializerRes.is_valid():
            serializerRes.save()
            return Response(data=serializerRes.data, status=200)
        else:
            return Response(serializerRes.errors, status=400)


########################## Helper Functions ##########################

    def _readImage(self, image, falg=0):
        serializer = self.serializer_class(image)
        imgPath = IMAGES_FOLDER+serializer.data.get("image")
        print(imgPath)
        # print(image)
        imageArr = cv2.imread(imgPath, falg)
        return imageArr

    def _drawHistAndCum(self, imgOperator, img, pk):
        hist = imgOperator.getHistoGram(img)
        plt.hist(imgOperator.flatten(img))
        plt.savefig(IMAGES_FOLDER + "/result/hist" + pk + ".jpg")
        plt.clf()
        plt.plot(imgOperator.getCumSum(hist))
        plt.savefig(IMAGES_FOLDER + "/result/cum" + pk + ".jpg")
        plt.close()
