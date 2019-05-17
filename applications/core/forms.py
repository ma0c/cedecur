from django import forms

from base.utils import generate_bootstrap_widgets_for_all_fields

from . import (
    models
)


class Category(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Category)


class Subcategory(forms.ModelForm):
    class Meta:
        model = models.Subcategory
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Subcategory)


class Enterprise(forms.ModelForm):
    class Meta:
        model = models.Enterprise
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Enterprise)


class EnterpriseForOwners(Enterprise):
    class Meta(Enterprise.Meta):
        exclude = [
            "slug",
            "active",
            "owner",
            "category",
            "sub_category",
            "latitude",
            "longitude"
        ]


class Product(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Product)


class ProductNoEnterprise(Product):
    class Meta(Product.Meta):
        fields = [
            'name',
            'description',
            'picture'
        ]


class Discounts(forms.ModelForm):
    class Meta:
        model = models.Discounts
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Discounts)


class DiscountsMinimal(Discounts):
    class Meta(Discounts.Meta):
        fields = [
            "product",
            "image",
            "description",
            "expires_on"
        ]


class Contact(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = [
            "name",
            "email",
            "title",
            "description"
        ]
        widgets = generate_bootstrap_widgets_for_all_fields(models.Contact)

