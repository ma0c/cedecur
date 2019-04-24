import random
import string

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

from base import models as base_models

from applications.core import (
    conf as core_conf
)


class Category(base_models.FullSlugBaseModel):

    class Meta:
        verbose_name = core_conf.CATEGORY_VERBOSE_NAME
        verbose_name_plural = core_conf.CATEGORY_VERBOSE_NAME_PLURAL


class Subcategory(base_models.FullSlugBaseModel):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = core_conf.SUBCATEGORY_VERBOSE_NAME
        verbose_name_plural = core_conf.SUBCATEGORY_VERBOSE_NAME_PLURAL


class Enterprise(base_models.FullSlugBaseModel):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)

    picture = models.FileField(null=True, blank=True)

    # Social media links
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    # Location
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        verbose_name = core_conf.ENTERPRISE_VERBOSE_NAME
        verbose_name_plural = core_conf.ENTERPRISE_VERBOSE_NAME_PLURAL


class Product(base_models.FullSlugBaseModel):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    picture = models.FileField()

    class Meta:
        verbose_name = core_conf.PRODUCT_VERBOSE_NAME
        verbose_name_plural = core_conf.PRODUCT_VERBOSE_NAME_PLURAL


class Discounts(base_models.FullSlugBaseModel):
    CODE_LENGTH = 30

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    code = models.CharField(max_length=CODE_LENGTH, unique=True)

    expires_on = models.DateTimeField()

    @staticmethod
    def create_code(length=CODE_LENGTH):
        return "".join(random.choices((string.ascii_letters + string.digits), k=length))

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.code:
            self.code = self.create_code()
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = core_conf.DISCOUNTS_VERBOSE_NAME
        verbose_name_plural = core_conf.DISCOUNTS_VERBOSE_NAME_PLURAL
