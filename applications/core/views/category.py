from django.contrib.auth.mixins import PermissionRequiredMixin
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
    List all Categorys
    """
    queryset = models.Category.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.CATEGORY_DETAIL_URL_NAME

        if self.request.user.has_perm("core.add_category"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.CATEGORY_CREATE_URL_NAME
            )
        
        return context


class Create(SuperAdminRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Category
    """
    model = models.Category
    permission_required = (
        'core.add_category'
    )
    form_class = forms.Category

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.CATEGORY_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(SuperAdminRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Category
    """
    model = models.Category

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("core.change_category"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.CATEGORY_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("core.delete_category"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.CATEGORY_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(SuperAdminRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Category
    """
    model = models.Category
    form_class = forms.Category
    permission_required = (
        'core.change_category'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.CATEGORY_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(SuperAdminRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Category
    """
    model = models.Category
    permission_required = (
        'core.delete_category'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.CATEGORY_LIST_URL_NAME)
