from rest_framework import serializers
from image.models import Image
from filter.models import FilteredImage
from detect.models import DetectedImage
from .ArrToImage import NumpyArrayToImageField


class ImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = ['id', 'image']


class FilteredImageSerializer(serializers.ModelSerializer):

    image = NumpyArrayToImageField()

    class Meta:
        model = FilteredImage
        fields = ['id', 'image']


class DetectedImageSerializer(serializers.ModelSerializer):

    image = NumpyArrayToImageField()

    class Meta:
        model = DetectedImage
        fields = ['id', 'image']
