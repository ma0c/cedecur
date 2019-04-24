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
    conf,
    utils
)


class List(LoginRequiredMixin, base_views.BaseListView):
    """
    List all Discountss
    """
    queryset = models.Discounts.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.DISCOUNTS_DETAIL_URL_NAME

        if self.request.user.has_perm("core.add_discounts"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.DISCOUNTS_CREATE_URL_NAME
            )
        
        return context


class Create(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Discounts
    """
    model = models.Discounts
    permission_required = (
        'core.add_discounts'
    )
    form_class = forms.Discounts

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.DISCOUNTS_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Discounts
    """
    model = models.Discounts

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("core.change_discounts"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.DISCOUNTS_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("core.delete_discounts"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.DISCOUNTS_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Discounts
    """
    model = models.Discounts
    form_class = forms.Discounts
    permission_required = (
        'core.change_discounts'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.DISCOUNTS_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Discounts
    """
    model = models.Discounts
    permission_required = (
        'core.delete_discounts'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.DISCOUNTS_LIST_URL_NAME)


class QRCode(
    base_views.BaseDetailView
):
    model = models.Discounts
    template_name = "core/discounts/qr_code.html"
    context_object_name = "element"

    def get_context_data(self, **kwargs):
        context = super(QRCode, self).get_context_data(**kwargs)
        context['qr_image'] = utils.get_base64_qr_code(self.get_object().code)

        return context