from rest_framework import serializers
from image.models import Image

class ImageSerializer(serializers.ModelSerializer):

    image= serializers.ImageField()

    class Meta:
        model = Image
        fields = ['id', 'image']

    