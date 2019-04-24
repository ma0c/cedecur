from django.urls import path
from django.views.generic import TemplateView

from applications.core import conf

from .views import enterprise

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name="core/index.html")
    ),

    path(
        'emprendedores',
        enterprise.Entreprenours.as_view(),
        name=conf.ENTERPRISE_ENTREPRENOURS_URL_NAME
    ),
    path(
        'emprendedores/categoria/<slug:slug>/',
        enterprise.EntreprenoursFilteredByCategory.as_view(),
        name=conf.ENTERPRISE_ENTREPRENOURS_CATEGORY_URL_NAME
    ),
    path(
        'emprendedores/subcategoria/<slug:slug>/',
        enterprise.EntreprenoursFilteredBySubCategory.as_view(),
        name=conf.ENTERPRISE_ENTREPRENOURS_SUBCATEGORY_URL_NAME
    ),
    path(
        'informacion',
        TemplateView.as_view(template_name="core/informacion.html")
    )
]

from applications.core import urls_slug
urlpatterns += urls_slug.urlpatterns
