import processing.contour as cn
import numpy as np
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from image.models import Image
from processing.Hough import Hough
from api.serializer import DetectedImageSerializer
import cv2
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')

IMAGES_FOLDER = './mediaFiles'


class DetectViewSet(viewsets.ModelViewSet):
    serializer_class = DetectedImageSerializer
    queryset = Image.objects.all()

    #################### the api for detect lines, circles and ellipses ####################

    @action(detail=True, methods=["post"], url_path=r'detect_shapes')
    def detect(self, request, pk=None):
        print(pk)
        # get the image given its id (pk = primary key)
        image = get_object_or_404(self.queryset, pk=pk)
        # read the image to 2d array
        imageArr = self._readImage(image, 1)

        option = request.data.get("option")
        firstValue = request.data.get("firstValue")
        secondValue = request.data.get("secondValue")
        thirdValue = request.data.get("thirdValue")

        imgOperator = Hough(imageArr)

        if(option == '1'):
            operatedImg = imgOperator.detect_lines(firstValue)
        elif(option == '2'):
            operatedImg = imgOperator.detect_circles(
                firstValue, secondValue, thirdValue)

        else:
            return Response(data={"image": "", "id": ""})

        serializerRes = self.serializer_class(data={"image": operatedImg})
        if serializerRes.is_valid():
            serializerRes.save()
            return Response(data=serializerRes.data, status=200)
        else:
            return Response(serializerRes.errors, status=400)

    #################### the api for contour ####################

    @action(detail=True, methods=["post"], url_path=r'draw_contour')
    def contour(self, request, pk=None):
        # get the image given its id (pk = primary key)
        image = get_object_or_404(self.queryset, pk=pk)
        # read the image to 2d array
        original_image = self._readImage(image, 1)
        parametersDict = {
            'apple3': {
                'xShift': 10,
                'yShift': 50,
                'radius': 50,
                'iterations': 25,
                'gamma':100
            },
            'circle': {
                'xShift': 0,
                'yShift': 50,
                'radius': 90,
                'iterations': 35,
                'gamma':100
            },
            'BlackApple': {
                'xShift': 40,
                'yShift': 30,
                'radius': 100,
                'iterations': 25,
                'gamma':5
            },
            'Convex-Polygon': {
                'xShift': 10,
                'yShift': 50,
                'radius': 110,
                'iterations': 35,
                'gamma':5
            }
        }
        points = 60
        sz = original_image.shape
        xCoordinates = np.zeros(points, dtype=np.int32)
        yCoordinates = np.zeros(points, dtype=np.int32)
        name = self._fileName(image)
        xCoordinates, yCoordinates = cn.circle_contour(
            (sz[0] // 2+parametersDict[name]['xShift'], sz[1] // 2+parametersDict[name]['yShift']), parametersDict[name]['radius'], points, xCoordinates, yCoordinates)
        xCoordinates, yCoordinates = cn.greedy_contour(
            original_image, parametersDict[name]['iterations'], 1, 2, parametersDict[name]['gamma'], xCoordinates, yCoordinates, points, 11, True)
        chaincode, normalisedToRotation, normalisedToStartingPoint = cn.getChainCode(
            xCoordinates, yCoordinates)
        print(normalisedToStartingPoint)
        area = f"contour area : {cn.contour_area(len(xCoordinates),xCoordinates,yCoordinates)} m^2"
        print(
            f"contour area : {cn.contour_area(len(xCoordinates),xCoordinates,yCoordinates)} m^2")

        # calculate area of the contour
        perimeter = f"contour perimeter : {cn.contour_perimeter(xCoordinates, yCoordinates, points)} m"
        # area = contour_area(points, xCoordinates, yCoordinates)
        operatedImg = cn.draw_contour(
            original_image, points, xCoordinates, yCoordinates)

        print(f"contour perimeter : {perimeter} m")

        serializerRes = self.serializer_class(data={"image": operatedImg})
        if serializerRes.is_valid():
            serializerRes.save()
            return Response(data={**serializerRes.data,
                                  **{"perimeter": perimeter, "area": area}}, status=200)
        else:
            return Response(serializerRes.errors, status=400)


########################## Helper Functions ##########################


    def _readImage(self, image, falg=0):
        serializer = self.serializer_class(image)
        imgPath = IMAGES_FOLDER+serializer.data.get("image")
        imageArr = cv2.imread(imgPath, falg)
        return imageArr

    def _fileName(self, image):
        serializer = self.serializer_class(image)
        imgName = serializer.data.get("image").rsplit("/")[2]
        if 'apple3' in imgName:
            return 'apple3'
        elif 'BlackApple' in imgName:
            return 'BlackApple'
        elif 'circle' in imgName:
            return 'circle'
        elif 'Convex-Polygon' in imgName:
            return 'Convex-Polygon'
        # return imgName
