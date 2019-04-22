from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy
from django import http


from base import views as base_views

from .. import (
    models,
    forms,
    conf
)


class List(LoginRequiredMixin, base_views.BaseListView):
    """
    List all Products
    """
    queryset = models.Product.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.PRODUCT_DETAIL_URL_NAME

        if self.request.user.has_perm("core.add_product"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.PRODUCT_CREATE_URL_NAME
            )
        
        return context


class Create(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Product
    """
    model = models.Product
    permission_required = (
        'core.add_product'
    )
    form_class = forms.Product

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.PRODUCT_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Product
    """
    model = models.Product

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("core.change_product"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.PRODUCT_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("core.delete_product"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.PRODUCT_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Product
    """
    model = models.Product
    form_class = forms.Product
    permission_required = (
        'core.change_product'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.PRODUCT_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Product
    """
    model = models.Product
    permission_required = (
        'core.delete_product'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.PRODUCT_LIST_URL_NAME)


