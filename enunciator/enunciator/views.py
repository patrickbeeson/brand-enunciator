from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    """
    View to render index template
    """
    template_name = 'index.html'
