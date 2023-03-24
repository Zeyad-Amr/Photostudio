from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from image.models import Image
# from processing.Filters import Filters
# from processing.Histograms import Histograms, ColoredOperator
# from processing.Frequency import Frequency
from api.serializer import DetectedImageSerializer
import cv2
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')
import random
import string

IMAGES_FOLDER = './mediaFiles'


class FilterViewSet(viewsets.ModelViewSet):
    serializer_class = DetectedImageSerializer
    queryset = Image.objects.all()

    #################### the api that process First tab (filter) functions ####################

    @action(detail=True, methods=["post"], url_path=r'detect_shapes')
    def filterProcess(self, request, pk=None):
        # get the image given its id (pk = primary key)
        image = get_object_or_404(self.queryset, pk=pk)
        # read the image to 2d array
        imageArr = self._readImage(image)

        option = request.data.get("option")
        # random name to prevent histogram or cumulative images from overwriting
        # randomName = ''.join(random.choices(string.ascii_letters, k=3)) + pk

        # imgOperator = 

        # operatedImg = imgOperator.detect()


        serializerRes = self.serializer_class(data={"image": operatedImg})
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

 