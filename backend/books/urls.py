from rest_framework.routers import DefaultRouter
from .views import TestTaskViewSet


router = DefaultRouter()

router.register('test_task', TestTaskViewSet, basename='test_task')

urlpatterns = router.urls
