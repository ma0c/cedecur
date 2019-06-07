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
        'empresa/',
        enterprise.List.as_view(),
        name=conf.ENTERPRISE_LIST_URL_NAME
    ),
    path(
        'empresa/create/',
        enterprise.Create.as_view(),
        name=conf.ENTERPRISE_CREATE_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/',
        enterprise.Detail.as_view(),
        name=conf.ENTERPRISE_DETAIL_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/actualizar/',
        enterprise.Update.as_view(),
        name=conf.ENTERPRISE_UPDATE_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/eliminar/',
        enterprise.Delete.as_view(),
        name=conf.ENTERPRISE_DELETE_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/agregar-producto/',
        enterprise.AddProduct.as_view(),
        name=conf.ENTERPRISE_ADD_PRODUCT_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/producto/<slug:{conf.PRODUCT_SLUG_URL_KWARG}>',
        enterprise.UpdateProduct.as_view(),
        name=conf.ENTERPRISE_UPDATE_PRODUCT_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/producto/<slug:{conf.PRODUCT_SLUG_URL_KWARG}>/eliminar',
        enterprise.DeleteProduct.as_view(),
        name=conf.ENTERPRISE_DELETE_PRODUCT_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/agregar-descuento/',
        enterprise.AddDiscount.as_view(),
        name=conf.ENTERPRISE_ADD_DISCOUNT_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/descuento/<slug:{conf.DISCOUNTS_SLUG_URL_KWARG}>/eliminar',
        enterprise.DeleteDiscount.as_view(),
        name=conf.ENTERPRISE_DELETE_DISCOUNT_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/agregar-mensaje/',
        enterprise.AddContact.as_view(),
        name=conf.ENTERPRISE_ADD_CONTACT_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/mensajes/',
        enterprise.ListContact.as_view(),
        name=conf.ENTERPRISE_LIST_CONTACT_URL_NAME
    ),
    path(
        f'empresa/<slug:{conf.ENTERPRISE_SLUG_URL_KWARG}>/estadisticas/',
        enterprise.CounterSummary.as_view(),
        name=conf.ENTERPRISE_SUMMARY_COUNTER_URL_NAME
    ),
]

# from .views import product
#
# urlpatterns += [
#     # product
#     path(
#         'product/',
#         product.List.as_view(),
#         name=conf.PRODUCT_LIST_URL_NAME
#     ),
#     path(
#         'product/create/',
#         product.Create.as_view(),
#         name=conf.PRODUCT_CREATE_URL_NAME
#     ),
#     path(
#         'product/<slug:slug>/',
#         product.Detail.as_view(),
#         name=conf.PRODUCT_DETAIL_URL_NAME
#     ),
#     path(
#         'product/<slug:slug>/update/',
#         product.Update.as_view(),
#         name=conf.PRODUCT_UPDATE_URL_NAME
#     ),
#     path(
#         'product/<slug:slug>/delete/',
#         product.Delete.as_view(),
#         name=conf.PRODUCT_DELETE_URL_NAME
#     ),
# ]

from .views import discounts

urlpatterns += [
#     # discounts
#     path(
#         'discounts/',
#         discounts.List.as_view(),
#         name=conf.DISCOUNTS_LIST_URL_NAME
#     ),
#     path(
#         'discounts/create/',
#         discounts.Create.as_view(),
#         name=conf.DISCOUNTS_CREATE_URL_NAME
#     ),
#     path(
#         'discounts/<slug:slug>/',
#         discounts.Detail.as_view(),
#         name=conf.DISCOUNTS_DETAIL_URL_NAME
#     ),
#     path(
#         'discounts/<slug:slug>/update/',
#         discounts.Update.as_view(),
#         name=conf.DISCOUNTS_UPDATE_URL_NAME
#     ),
#     path(
#         'discounts/<slug:slug>/delete/',
#         discounts.Delete.as_view(),
#         name=conf.DISCOUNTS_DELETE_URL_NAME
#     ),
    path(
        'discounts/<slug:slug>/qr/',
        discounts.QRCode.as_view(),
        name=conf.DISCOUNTS_QR_CODE_URL_NAME
    ),
    path(
        'discounts/validate/',
        discounts.ValidateDiscount.as_view(),
        name=conf.DISCOUNTS_VALIDATE_CODE_URL_NAME
    ),
]

# from .views import contact
#
# urlpatterns += [
#     # contact
#     path(
#         'contact/',
#         contact.List.as_view(),
#         name=conf.CONTACT_LIST_URL_NAME
#     ),
#     path(
#         'contact/create/',
#         contact.Create.as_view(),
#         name=conf.CONTACT_CREATE_URL_NAME
#     ),
#     path(
#         'contact/<slug:slug>/',
#         contact.Detail.as_view(),
#         name=conf.CONTACT_DETAIL_URL_NAME
#     ),
#     path(
#         'contact/<slug:slug>/update/',
#         contact.Update.as_view(),
#         name=conf.CONTACT_UPDATE_URL_NAME
#     ),
#     path(
#         'contact/<slug:slug>/delete/',
#         contact.Delete.as_view(),
#         name=conf.CONTACT_DELETE_URL_NAME
#     ),
# ]

