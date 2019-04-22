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




