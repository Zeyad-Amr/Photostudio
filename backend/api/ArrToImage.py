from rest_framework import serializers
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as Img
import numpy as np
import io

class NumpyArrayToImageField(serializers.ImageField):
    def to_internal_value(self, data):
        # Assuming the numpy array is in the request data
        numpy_array = data

        # Convert the numpy array to a PIL Image object
        pil_image = Img.fromarray(np.uint8(numpy_array))

        # Convert the PIL Image object to a file-like object
        file_obj = io.BytesIO()
        pil_image.save(file_obj, 'JPEG')
        file_obj.seek(0)

        # Create an InMemoryUploadedFile object from the file-like object
        uploaded_file = InMemoryUploadedFile(
            file_obj, None, 'foo.jpg', 'image/jpeg', file_obj.getbuffer().nbytes, None
        )

        return uploaded_file