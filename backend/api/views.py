from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from image.models import Image
from processing.Filters import Filters
from processing.Histograms import Histograms, ColoredOperator
from processing.Frequency import Frequency
from .serializer import *
import cv2
import matplotlib
from matplotlib import pyplot as plt
import random
import string
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

    #################### the api that process First tab (filter) functions ####################

    @action(detail=True, methods=["post"], url_path=r'filter_process')
    def filterProcess(self, request, pk=None):
        # get the image given its id (pk = primary key)
        image = get_object_or_404(self.queryset, pk=pk)
        # read the image to 2d array
        imageArr = self._readImage(image)

        option = request.data.get("option")
        # random name to prevent histogram or cumulative images from overwriting
        randomName = ''.join(random.choices(string.ascii_letters, k=3)) + pk

        range = request.data.get("range")
        imgOperator = Filters()

        # add noise
        if(option == '1'):
            operatedImg = imgOperator.uniform_noise(imageArr, range)
        elif(option == '2'):
            operatedImg = imgOperator.gaussian_noise(imageArr, range)
        elif(option == '3'):
            operatedImg = imgOperator.salt_pepper_noise(imageArr, range)

        # filter image
        elif(option == '4'):
            operatedImg = imgOperator.average_filter(imageArr, range)
        elif(option == '5'):
            operatedImg = imgOperator.gaussian_filter(imageArr, range)
        elif(option == '6'):
            operatedImg = imgOperator.median_filter(imageArr, range)

        serializerRes = ImageSerializerArr(data={"image": operatedImg})
        if serializerRes.is_valid():
            serializerRes.save()
            return Response(data=serializerRes.data, status=200)
        else:
            return Response(serializerRes.errors, status=400)

    #################### the api that process First tab (edge detiction) functions ####################

    @action(detail=True, methods=["post"], url_path=r'edge_detiction')
    def edgeDetiction(self, request, pk=None):
        # get the image given its id (pk = primary key)
        image = get_object_or_404(self.queryset, pk=pk)
        # read the image to 2d array
        imageArr = self._readImage(image)

        option = request.data.get("option")
        # random name to prevent histogram or cumulative images from overwriting
        randomName = ''.join(random.choices(string.ascii_letters, k=3)) + pk

        range = request.data.get("range")
        imgOperator = Filters()

        # edge detection
        if(option == '7'):
            operatedImg = imgOperator.sobel_edge_detector(imageArr)
        elif(option == '8'):
            operatedImg = imgOperator.roberts_edge_detector(imageArr)
        elif(option == '9'):
            operatedImg = imgOperator.prewitt_edge_detector(imageArr)
        elif(option == '10'):
            operatedImg = imgOperator.canny_edge_detector(imageArr, range)
        else:
            return Response(data={"image": "", "id": ""})

        plt.imsave(IMAGES_FOLDER + "/edge" + randomName +
                   ".jpg", operatedImg, cmap='gray')

        return Response(data={"image": "http://127.0.0.1:8000/edge" + randomName + ".jpg"}, status=200)

#################### the api that process Second tab (histograms) functions ####################

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
                                  **{"histURL": "http://127.0.0.1:8000/hist" + randomName + ".jpg",
                                     "cumURL": "http://127.0.0.1:8000/cum" + randomName + ".jpg"}},
                            status=200)
        else:
            return Response(serializerRes.errors, status=400)

    #################### the api that process Second tab Transformation (Split to RGB) functions ####################

    @action(detail=True, methods=["post"], url_path=r'transformation')
    def transProcess(self, request, pk=None):
        # get the image given its id (pk = primary key)
        image = get_object_or_404(self.queryset, pk=pk)
        # get the image path to read it w/ cv2 and pass it to Histogram class
        imageArr = self._readImage(image)

        imgOperator = Histograms(imageArr)
        option = request.data.get("option")

        # random name to prevent histogram or cumulative images from overwriting
        redName = 'red_' + \
            ''.join(random.choices(string.ascii_letters, k=3)) + pk
        greenName = 'green_' + \
            ''.join(random.choices(string.ascii_letters, k=3)) + pk
        blueName = 'blue_' + \
            ''.join(random.choices(string.ascii_letters, k=3)) + pk

        if(option == '5'):
            coloredImg = ColoredOperator(self._readImage(image, 1))
            grayImg = coloredImg.grayScale()
            # plt.imsave(IMAGES_FOLDER + "/gray.jpg", grayImg)
            self._drawHistAndCum(
                imgOperator, coloredImg.getRedFrame(), redName)
            self._drawHistAndCum(
                imgOperator, coloredImg.getGreenFrame(), greenName)
            self._drawHistAndCum(
                imgOperator, coloredImg.getBlueFrame(), blueName)
        else:
            return Response(data={"image": ""})

        serializerRes = ImageSerializerArr(data={"image": grayImg})
        if serializerRes.is_valid():
            serializerRes.save()
            return Response(data={**serializerRes.data,
                                  **{
                                      "redHistURL": "http://127.0.0.1:8000/hist" + redName + ".jpg",
                                      "greenHistURL": "http://127.0.0.1:8000/hist" + greenName + ".jpg",
                                      "blueHistURL": "http://127.0.0.1:8000/hist" + blueName + ".jpg",
                                      "redCumURL": "http://127.0.0.1:8000/cum" + redName + ".jpg",
                                      "greenCumURL": "http://127.0.0.1:8000/cum" + greenName + ".jpg",
                                      "blueCumURL": "http://127.0.0.1:8000/cum" + blueName + ".jpg",
                                  }},
                            status=200)
        else:
            return Response(serializerRes.errors, status=400)

    #################### the api that process Third tab (frequancy) functions ####################

    @action(detail=False, methods=["post"], url_path=r'frequancy_process')
    def freqProcess(self, request):
        # get the image given its id (pk = primary key)
        f_imgId = request.data.get("f_imgId")
        s_imgId = request.data.get("s_imgId")
        image1 = get_object_or_404(self.queryset, pk=f_imgId)
        image2 = get_object_or_404(self.queryset, pk=s_imgId)
        # read the image to 2d array
        imageArr1 = self._readImage(image1)
        imageArr2 = self._readImage(image2)

        # get cuttof frequancies
        firstCutoff = request.data.get("f_cutoff")
        secondCutoff = request.data.get("s_cutoff")

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
        lowPass = imgOperator.low_pass_filter(L_image, firstCutoff)
        highPass = imgOperator.high_pass_filter(H_image, secondCutoff)

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
        imageArr = cv2.imread(imgPath, falg)
        return imageArr

    def _drawHistAndCum(self, imgOperator, img, pk):
        hist = imgOperator.getHistoGram(img)
        plt.hist(imgOperator.flatten(img))
        plt.savefig(IMAGES_FOLDER + "/hist" + pk + ".jpg")
        plt.clf()
        plt.plot(imgOperator.getCumSum(hist))
        plt.savefig(IMAGES_FOLDER + "/cum" + pk + ".jpg")
        plt.close()
