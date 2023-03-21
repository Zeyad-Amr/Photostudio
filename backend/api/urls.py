from rest_framework.routers import DefaultRouter
from apps.filter.views import FilterViewSet
from apps.image.views import ImageViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'api/image', ImageViewSet, basename='image')
router.register(r'api/image/filter', FilterViewSet, basename='image')

urlpatterns = router.urls

