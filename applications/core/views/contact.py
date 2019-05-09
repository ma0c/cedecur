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
    List all Contacts
    """
    queryset = models.Contact.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.CONTACT_DETAIL_URL_NAME

        if self.request.user.has_perm("core.add_contact"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.CONTACT_CREATE_URL_NAME
            )
        
        return context


class Create(base_views.BaseCreateView):
    """
    Create a Contact
    """
    model = models.Contact
    permission_required = (
        'core.add_contact'
    )
    form_class = forms.Contact

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.CONTACT_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Contact
    """
    model = models.Contact

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("core.change_contact"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.CONTACT_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("core.delete_contact"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.CONTACT_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Contact
    """
    model = models.Contact
    form_class = forms.Contact
    permission_required = (
        'core.change_contact'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.CONTACT_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Contact
    """
    model = models.Contact
    permission_required = (
        'core.delete_contact'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.CONTACT_LIST_URL_NAME)
