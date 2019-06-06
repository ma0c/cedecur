from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy
from django import http
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q

from base import views as base_views

from applications.authentication.mixins import SuperAdminRequiredMixin

from applications.core import (
    models,
    forms,
    conf,
    mixins
)

from applications.core.views import (
    product,
    discounts,
    contact
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

    def kwargs_for_reverse_url(self):
        return {
            conf.ENTERPRISE_SLUG_URL_KWARG: self.get_object().slug
        }

    def get_success_url(self):
        return reverse_lazy(conf.ENTERPRISE_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(
    mixins.EnterpriseMixin,
    base_views.BaseDetailView
):
    """
    Detail of a Enterprise
    """
    model = models.Enterprise
    template_name = "core/informacion.html"
    context_object_name = "enterprise"
    slug_url_kwarg = conf.ENTERPRISE_SLUG_URL_KWARG

    def __init__(self):
        super(Detail, self).__init__()

    def kwargs_for_reverse_url(self):
        return {
            conf.ENTERPRISE_SLUG_URL_KWARG: self.get_object().slug
        }

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        context["discounts"] = models.Discounts.objects.filter(
            product__enterprise=self.get_enterprise(),
            expires_on__gte=timezone.now()
        )

        context["discount_qr_code_url"] = conf.DISCOUNTS_QR_CODE_URL_NAME

        context["add_contact_reversed_url"] = reverse_lazy(
            conf.ENTERPRISE_ADD_CONTACT_URL_NAME,
            kwargs=self.kwargs_for_reverse_url()
        )

        if self.get_object().owner == self.request.user or self.request.user.is_staff:

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

            if self.request.user.has_perm("core.add_product"):
                context['add_product_reversed_url'] = reverse_lazy(
                    conf.ENTERPRISE_ADD_PRODUCT_URL_NAME,
                    kwargs=self.kwargs_for_reverse_url()
                )

            if self.request.user.has_perm("core.change_product"):
                context['change_product_url'] = conf.ENTERPRISE_UPDATE_PRODUCT_URL_NAME

            if self.request.user.has_perm("core.delete_product"):
                context['delete_product_url'] = conf.ENTERPRISE_DELETE_PRODUCT_URL_NAME

            if self.request.user.has_perm("core.add_discounts"):
                context['add_discount_reversed_url'] = reverse_lazy(
                    conf.ENTERPRISE_ADD_DISCOUNT_URL_NAME,
                    kwargs=self.kwargs_for_reverse_url()
                )

            if self.request.user.has_perm("core.delete_discounts"):
                context['delete_discount_url'] = conf.ENTERPRISE_DELETE_DISCOUNT_URL_NAME

                context['list_contact_url_reversed'] = reverse_lazy(
                    conf.ENTERPRISE_LIST_CONTACT_URL_NAME,
                    kwargs=self.kwargs_for_reverse_url()
                )

        return context


class Update(
    mixins.EnterpriseMixin,
    mixins.OwnershipEnterpriseMixin,
    PermissionRequiredMixin,
    base_views.BaseUpdateView
):
    """
    Update a Enterprise
    """
    model = models.Enterprise
    permission_required = (
        'core.change_enterprise'
    )
    slug_url_kwarg = conf.ENTERPRISE_SLUG_URL_KWARG
    template_name = "core/enterprise/update.html"

    def __init__(self):
        super(Update, self).__init__()

    def get_form_class(self):
        if self.request.user.is_staff:
            return forms.Enterprise
        return forms.EnterpriseForOwners

    def kwargs_for_reverse_url(self):
        return {
            conf.ENTERPRISE_SLUG_URL_KWARG: self.get_object().slug
        }

    def get_success_url(self):
        return reverse_lazy(conf.ENTERPRISE_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(
    mixins.EnterpriseMixin,
    mixins.OwnershipEnterpriseMixin,
    PermissionRequiredMixin,
    base_views.BaseDeleteView
):
    """
    Delete a Enterprise
    """
    model = models.Enterprise
    permission_required = (
        'core.delete_enterprise'
    )
    slug_url_kwarg = conf.ENTERPRISE_SLUG_URL_KWARG

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ENTERPRISE_LIST_URL_NAME)


class Entreprenours(base_views.BaseListView):
    template_name = "core/perfiles.html"
    queryset = models.Enterprise.objects.filter(active=True)
    context_object_name = "enterprises"


class EntreprenoursFilteredByCategory(Entreprenours):

    def get_category(self):
        return models.Category.objects.get(slug=self.kwargs.get("slug", ""))

    def get_queryset(self):
        return models.Enterprise.objects.filter(active=True, category=self.get_category())


class EntreprenoursFilteredBySubCategory(Entreprenours):

    def get_subcategory(self):
        return models.Subcategory.objects.get(slug=self.kwargs.get("slug", ""))

    def get_queryset(self):
        return models.Enterprise.objects.filter(active=True, sub_category=self.get_subcategory())


class EntreprenoursFilteredBySearch(Entreprenours):

    def get_queryset(self):
        query_parameter = self.request.GET.get("search", "")
        return models.Enterprise.objects.filter(
            active=True
        ).filter(
            Q(name__icontains=query_parameter) |
            Q(description__icontains=query_parameter) |
            Q(keyboards__icontains=query_parameter)
        )


class AddProduct(
    mixins.EnterpriseMixin,
    mixins.OwnershipEnterpriseMixin,
    product.Create
):
    form_class = forms.ProductNoEnterprise
    slug_url_kwarg = conf.ENTERPRISE_SLUG_URL_KWARG

    def form_valid(self, form):
        product = form.save(commit=False)
        product.enterprise = self.get_enterprise()
        product.save()
        return http.HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(
            conf.ENTERPRISE_DETAIL_URL_NAME,
            kwargs={
                conf.ENTERPRISE_SLUG_URL_KWARG: self.get_enterprise().slug
            }
        )


class UpdateProduct(
    mixins.EnterpriseMixin,
    mixins.ProductMixin,
    mixins.OwnershipProductMixin,
    product.Update
):
    form_class = forms.ProductNoEnterprise
    slug_url_kwarg = conf.PRODUCT_SLUG_URL_KWARG
    template_name = "core/product/update.html"
    context_object_name = "product"

    def get_success_url(self):
        return reverse_lazy(
            conf.ENTERPRISE_DETAIL_URL_NAME,
            kwargs={
                conf.ENTERPRISE_SLUG_URL_KWARG: self.get_enterprise().slug
            }
        )


class DeleteProduct(
    mixins.EnterpriseMixin,
    mixins.ProductMixin,
    mixins.OwnershipProductMixin,
    product.Delete
):
    slug_url_kwarg = conf.PRODUCT_SLUG_URL_KWARG

    def get_success_url(self):
        return reverse_lazy(
            conf.ENTERPRISE_DETAIL_URL_NAME,
            kwargs={
                conf.ENTERPRISE_SLUG_URL_KWARG: self.get_enterprise().slug
            }
        )


class AddDiscount(
    mixins.EnterpriseMixin,
    mixins.OwnershipEnterpriseMixin,
    discounts.Create
):
    form_class = forms.DiscountsMinimal
    slug_url_kwarg = conf.ENTERPRISE_SLUG_URL_KWARG

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["product"].queryset = models.Product.objects.filter(enterprise=self.get_enterprise())
        return form

    def get_success_url(self):
        return reverse_lazy(
            conf.ENTERPRISE_DETAIL_URL_NAME,
            kwargs={
                conf.ENTERPRISE_SLUG_URL_KWARG: self.get_enterprise().slug
            }
        )


class DeleteDiscount(
    mixins.EnterpriseMixin,
    mixins.DiscountMixin,
    mixins.OwnershipDiscountMixin,
    discounts.Delete
):
    slug_url_kwarg = conf.DISCOUNTS_SLUG_URL_KWARG

    def get_success_url(self):
        return reverse_lazy(
            conf.ENTERPRISE_DETAIL_URL_NAME,
            kwargs={
                conf.ENTERPRISE_SLUG_URL_KWARG: self.get_enterprise().slug
            }
        )


class AddContact(
    mixins.EnterpriseMixin,
    contact.Create
):
    form_class = forms.Contact
    slug_url_kwarg = conf.ENTERPRISE_SLUG_URL_KWARG

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.enterprise = self.get_enterprise()
        contact.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            conf.MESSAGE_POSTED_SUCCESSFULLY
        )
        return http.HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(
            conf.ENTERPRISE_DETAIL_URL_NAME,
            kwargs={
                conf.ENTERPRISE_SLUG_URL_KWARG: self.get_enterprise().slug
            }
        )


class ListContact(
    mixins.EnterpriseMixin,
    mixins.OwnershipEnterpriseMixin,
    contact.List
):
    slug_url_kwarg = conf.ENTERPRISE_SLUG_URL_KWARG
    template_name = "core/contact/list.html"


class MyEnterprises(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    base_views.BaseListView
):
    permission_required = (
        'core.change_enterprise'
    )
    template_name = "core/perfiles.html"
    context_object_name = "enterprises"

    def get_queryset(self):
        return models.Enterprise.objects.filter(owner=self.request.user)