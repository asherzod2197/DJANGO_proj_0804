from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('masters', MasterViewSet, basename='master')
router.register('mentors', MentorViewSet, basename='mentor')
router.register('groups', GroupViewSet, basename='group')
router.register('students', StudentViewSet, basename='student')

urlpatterns = router.urls