from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import login, PatientViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('login/', login, name='login'),
    path('', include(router.urls)),
]
