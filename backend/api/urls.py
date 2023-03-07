from django.urls import path, include
from .views import ImageViewSet
from rest_framework.routers import DefaultRouter

# image_create = views.MyModelViewSet.as_view({
#     'post': 'create'
# })
app_name= 'api'

router = DefaultRouter()
router.register(r'api/image', ImageViewSet, basename='image')

urlpatterns = router.urls
# [
#     path('', views.get),
#     path('', include(router.urls))
#     # path('image', views.image_controller),
#     # path('image', views.getAllImages),
#     # path('upload', image_create),
# ]
