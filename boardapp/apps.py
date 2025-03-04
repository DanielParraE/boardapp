"""
boardapp Django application initialization.
"""

from django.apps import AppConfig


class BoardappConfig(AppConfig):
    """
    Configuration for the boardapp Django application.
    """

    name = "boardapp"
    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "boardapp",
                "relative_path": "urls",
                # "regex": "^boardapp/"
            }
        },
        "settings_config": {
            "lms.djangoapp": {
                "common": {"relative_path": "settings"},
            }
        },
    }
