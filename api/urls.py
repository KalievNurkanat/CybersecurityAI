from django.urls import path, include
from api.views import RequestDataViewSets, RequestGmailDataViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"request-data", RequestDataViewSets, basename="request-data")
router.register(r"request-gmail-data", RequestGmailDataViewSets, basename="request-gmail-data")

urlpatterns = [
    path("", include(router.urls))
]