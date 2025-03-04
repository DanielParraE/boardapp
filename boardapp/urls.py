"""
URLs for boardapp.
"""
from django.urls import path  # pylint: disable=unused-import
from .views import BoardappIndex

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    path("index/", BoardappIndex.as_view(), name="index"),
]
