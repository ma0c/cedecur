from django import http
from django.template.loader import get_template

from applications.core import (
    models as core_models,
    conf as core_conf
)


class OwnershipEnterpriseMixin(object):
    def dispatch(self, request, *args, **kwargs):
        # This will fire a Login Required
        print(self.get_enterprise().owner)
        print(self.request.user)
        if self.request.user.is_authenticated and \
                (self.request.user.is_staff or self.get_enterprise().owner == self.request.user):
            print("Permission granted")
            return super().dispatch(request, *args,  **kwargs)
        print("Permission NOT granted")
        return http.HttpResponseForbidden(get_template("403.html").render())


class EnterpriseMixin(object):

    def get_enterprise(self):
        return core_models.Enterprise.objects.get(slug=self.kwargs.get(core_conf.ENTERPRISE_SLUG_URL_KWARG, ""))