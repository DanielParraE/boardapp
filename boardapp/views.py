from django.views.generic import TemplateView  # pylint: disable=unused-import

# TemplateView.as_view(template_name="boardapp/base.html")

class BoardappIndex(TemplateView):
    template_name = "boardapp/base.html"
