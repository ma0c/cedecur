from django import http
from django.template.loader import get_template

from applications.core import (
    models as core_models,
    conf as core_conf
)


class OwnershipEnterpriseMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and \
                (self.request.user.is_staff or self.get_enterprise().owner == self.request.user):
            print("Permission granted")
            return super().dispatch(request, *args,  **kwargs)
        print("Permission NOT granted")
        return http.HttpResponseForbidden(get_template("errors/403.html").render())


class OwnershipProductMixin(object):
    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated and \
                (self.request.user.is_staff or self.get_enterprise().owner == self.request.user) and\
                self.get_enterprise() == self.get_product().enterprise:

            return super().dispatch(request, *args,  **kwargs)
        print("Permission NOT granted")
        return http.HttpResponseForbidden(get_template("errors/403.html").render())


class OwnershipDiscountMixin(object):
    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_authenticated and \
                (self.request.user.is_staff or self.get_enterprise().owner == self.request.user) and\
                self.get_enterprise() == self.get_discount().product.enterprise:

            return super().dispatch(request, *args,  **kwargs)
        return http.HttpResponseForbidden(get_template("errors/403.html").render())


class EnterpriseMixin(object):

    def get_enterprise(self):
        return core_models.Enterprise.objects.get(slug=self.kwargs.get(core_conf.ENTERPRISE_SLUG_URL_KWARG, ""))


class ProductMixin(object):

    def get_product(self):
        return core_models.Product.objects.get(slug=self.kwargs.get(core_conf.PRODUCT_SLUG_URL_KWARG, ""))


class DiscountMixin(object):

    def get_discount(self):
        return core_models.Discounts.objects.get(slug=self.kwargs.get(core_conf.DISCOUNTS_SLUG_URL_KWARG, ""))

