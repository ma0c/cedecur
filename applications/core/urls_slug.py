from django.urls import path

from . import conf

urlpatterns = [

]

from .views import category

urlpatterns += [
    # category
    path(
        'category/',
        category.List.as_view(),
        name=conf.CATEGORY_LIST_URL_NAME
    ),
    path(
        'category/create/',
        category.Create.as_view(),
        name=conf.CATEGORY_CREATE_URL_NAME
    ),
    path(
        'category/(<slug:slug>)/',
        category.Detail.as_view(),
        name=conf.CATEGORY_DETAIL_URL_NAME
    ),
    path(
        'category/(<slug:slug>)/update/',
        category.Update.as_view(),
        name=conf.CATEGORY_UPDATE_URL_NAME
    ),
    path(
        'category/(<slug:slug>)/delete/',
        category.Delete.as_view(),
        name=conf.CATEGORY_DELETE_URL_NAME
    ),
]

from .views import subcategory

urlpatterns += [
    # subcategory
    path(
        'subcategory/',
        subcategory.List.as_view(),
        name=conf.SUBCATEGORY_LIST_URL_NAME
    ),
    path(
        'subcategory/create/',
        subcategory.Create.as_view(),
        name=conf.SUBCATEGORY_CREATE_URL_NAME
    ),
    path(
        'subcategory/<slug:slug>/',
        subcategory.Detail.as_view(),
        name=conf.SUBCATEGORY_DETAIL_URL_NAME
    ),
    path(
        'subcategory/<slug:slug>/update/',
        subcategory.Update.as_view(),
        name=conf.SUBCATEGORY_UPDATE_URL_NAME
    ),
    path(
        'subcategory/<slug:slug>/delete/',
        subcategory.Delete.as_view(),
        name=conf.SUBCATEGORY_DELETE_URL_NAME
    ),
]

from .views import enterprise

urlpatterns += [
    # enterprise
    path(
        'enterprise/',
        enterprise.List.as_view(),
        name=conf.ENTERPRISE_LIST_URL_NAME
    ),
    path(
        'enterprise/create/',
        enterprise.Create.as_view(),
        name=conf.ENTERPRISE_CREATE_URL_NAME
    ),
    path(
        'enterprise/<slug:slug>/',
        enterprise.Detail.as_view(),
        name=conf.ENTERPRISE_DETAIL_URL_NAME
    ),
    path(
        'enterprise/<slug:slug>/update/',
        enterprise.Update.as_view(),
        name=conf.ENTERPRISE_UPDATE_URL_NAME
    ),
    path(
        'enterprise/<slug:slug>/delete/',
        enterprise.Delete.as_view(),
        name=conf.ENTERPRISE_DELETE_URL_NAME
    ),
]

