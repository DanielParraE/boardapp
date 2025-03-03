"""
URLs for boardapp.
"""
from django.urls import re_path  # pylint: disable=unused-import
from .views import BoardappIndex

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    re_path(r"", BoardappIndex.as_view(), name="index"),
]
