from rest_framework.routers import DefaultRouter
from apps.filter.views import FilterViewSet
from apps.image.views import ImageViewSet
from apps.detect.views import DetectViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'api/image', ImageViewSet, basename='image')
router.register(r'api/image/filter', FilterViewSet, basename='image')
router.register(r'api/image/detect', DetectViewSet, basename='image')

urlpatterns = router.urls

