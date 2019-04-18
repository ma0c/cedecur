from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name="core/index.html")
    ),

    path(
        'perfiles',
        TemplateView.as_view(template_name="core/perfiles1.html")
    ),
    path(
        'informacion',
        TemplateView.as_view(template_name="core/informacion1.html")
    )
]
