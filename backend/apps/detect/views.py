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
        points = 60
        sz = original_image.shape
        x_cooridinates = np.zeros(points, dtype=np.int32)
        y_cooridinates = np.zeros(points, dtype=np.int32)
        x_cooridinates, y_cooridinates = cn.circle_contour(
            (sz[0] // 2, sz[1] // 2+50), 90, points, x_cooridinates, y_cooridinates)
        x_cooridinates, y_cooridinates = cn.greedy_contour(
            original_image, 30, 1, 2, 100, x_cooridinates, y_cooridinates, points, 11, True)
        chaincode, normalisedToRotation, normalisedToStartingPoint = cn.getChainCode(
            x_cooridinates, y_cooridinates)
        print(normalisedToStartingPoint)
        area = f"contour area : {cn.contour_area(len(x_cooridinates),x_cooridinates,y_cooridinates)} m^2"
        print(
            f"contour area : {cn.contour_area(len(x_cooridinates),x_cooridinates,y_cooridinates)} m^2")

        # calculate area of the contour
        perimeter = f"contour perimeter : {cn.contour_perimeter(x_cooridinates, y_cooridinates, points)} m"
        # area = contour_area(points, x_cooridinates, y_cooridinates)
        operatedImg = cn.draw_contour(
            original_image, points, x_cooridinates, y_cooridinates)

        print(f"contour perimeter : {perimeter} m")

        serializerRes = self.serializer_class(data={"image": operatedImg})
        if serializerRes.is_valid():
            serializerRes.save()
            return Response(data={**serializerRes, **{perimeter: perimeter, area: area}}.data, status=200)
        else:
            return Response(serializerRes.errors, status=400)


########################## Helper Functions ##########################


    def _readImage(self, image, falg=0):
        serializer = self.serializer_class(image)
        imgPath = IMAGES_FOLDER+serializer.data.get("image")
        imageArr = cv2.imread(imgPath, falg)
        return imageArr