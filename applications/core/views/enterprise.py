from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy
from django import http


from base import views as base_views

from applications.authentication.mixins import SuperAdminRequiredMixin

from .. import (
    models,
    forms,
    conf
)


class List(SuperAdminRequiredMixin, base_views.BaseListView):
    """
    List all Enterprises
    """
    queryset = models.Enterprise.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.ENTERPRISE_DETAIL_URL_NAME

        if self.request.user.has_perm("core.add_enterprise"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.ENTERPRISE_CREATE_URL_NAME
            )
        
        return context


class Create(SuperAdminRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Enterprise
    """
    model = models.Enterprise
    permission_required = (
        'core.add_enterprise'
    )
    form_class = forms.Enterprise

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ENTERPRISE_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(SuperAdminRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Enterprise
    """
    model = models.Enterprise

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("core.change_enterprise"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.ENTERPRISE_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("core.delete_enterprise"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.ENTERPRISE_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(SuperAdminRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Enterprise
    """
    model = models.Enterprise
    form_class = forms.Enterprise
    permission_required = (
        'core.change_enterprise'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ENTERPRISE_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(SuperAdminRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Enterprise
    """
    model = models.Enterprise
    permission_required = (
        'core.delete_enterprise'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ENTERPRISE_LIST_URL_NAME)


class Entreprenours(base_views.BaseListView):
    template_name = "core/perfiles.html"
    queryset = models.Enterprise.objects.all()
    context_object_name = "enterprises"


class EntreprenoursFilteredByCategory(Entreprenours):

    def get_category(self):
        return models.Category.objects.get(slug=self.kwargs.get("slug", ""))

    def get_queryset(self):
        return models.Enterprise.objects.filter(category=self.get_category())


class EntreprenoursFilteredBySubCategory(Entreprenours):

    def get_subcategory(self):
        return models.Subcategory.objects.get(slug=self.kwargs.get("slug", ""))

    def get_queryset(self):
        return models.Enterprise.objects.filter(sub_category=self.get_subcategory())


