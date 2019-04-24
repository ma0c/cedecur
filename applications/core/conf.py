from django.utils.translation import ugettext_lazy as _

from base import conf

ENTERPRISE_MANAGER_GROUP_NAME = _("Enterprise Manager")

PERMISSIONS = {
    # '': {
    #     'app_label': 'core',
    #     'model': 'core',
    #     'codename': 'code_name_for_permissions',
    # }
}

GROUPS = {
    'manager_enterprise': {
        "name": ENTERPRISE_MANAGER_GROUP_NAME,
        'permissions': [
            "change_enterprise",
            "add_product",
            "change_product",
            "delete_product",
            "add_discounts",
            "change_discounts",
            "delete_discounts"
        ]
    },
}

USER_CREATED = _("User created: {}")
USER_ALREADY_CREATED = _("User  already created: {}")


CATEGORY_PREFIX = "CATEGORY"

CATEGORY_VERBOSE_NAME = _("Category")
CATEGORY_VERBOSE_NAME_PLURAL = _("Category")

CATEGORY_LIST_URL_NAME = CATEGORY_PREFIX + conf.LIST_SUFFIX
CATEGORY_CREATE_URL_NAME = CATEGORY_PREFIX + conf.CREATE_SUFFIX
CATEGORY_DETAIL_URL_NAME = CATEGORY_PREFIX + conf.DETAIL_SUFFIX
CATEGORY_UPDATE_URL_NAME = CATEGORY_PREFIX + conf.UPDATE_SUFFIX
CATEGORY_DELETE_URL_NAME = CATEGORY_PREFIX + conf.DELETE_SUFFIX

CATEGORY_CREATED = _("Category created: {}")
CATEGORY_ALREADY_CREATED = _("Category already created: {}")

SUBCATEGORY_PREFIX = "SUBCATEGORY"

SUBCATEGORY_VERBOSE_NAME = _("Subcategory")
SUBCATEGORY_VERBOSE_NAME_PLURAL = _("Subcategory")

SUBCATEGORY_LIST_URL_NAME = SUBCATEGORY_PREFIX + conf.LIST_SUFFIX
SUBCATEGORY_CREATE_URL_NAME = SUBCATEGORY_PREFIX + conf.CREATE_SUFFIX
SUBCATEGORY_DETAIL_URL_NAME = SUBCATEGORY_PREFIX + conf.DETAIL_SUFFIX
SUBCATEGORY_UPDATE_URL_NAME = SUBCATEGORY_PREFIX + conf.UPDATE_SUFFIX
SUBCATEGORY_DELETE_URL_NAME = SUBCATEGORY_PREFIX + conf.DELETE_SUFFIX

SUBCATEGORY_CREATED = _("Subcategory created: {}")
SUBCATEGORY_ALREADY_CREATED = _("Subcategory  already created: {}")

ENTERPRISE_PREFIX = "ENTERPRISE"

ENTERPRISE_VERBOSE_NAME = _("Enterprise")
ENTERPRISE_VERBOSE_NAME_PLURAL = _("Enterprise")

ENTERPRISE_LIST_URL_NAME = ENTERPRISE_PREFIX + conf.LIST_SUFFIX
ENTERPRISE_CREATE_URL_NAME = ENTERPRISE_PREFIX + conf.CREATE_SUFFIX
ENTERPRISE_DETAIL_URL_NAME = ENTERPRISE_PREFIX + conf.DETAIL_SUFFIX
ENTERPRISE_UPDATE_URL_NAME = ENTERPRISE_PREFIX + conf.UPDATE_SUFFIX
ENTERPRISE_DELETE_URL_NAME = ENTERPRISE_PREFIX + conf.DELETE_SUFFIX
ENTERPRISE_ENTREPRENOURS_URL_NAME = ENTERPRISE_PREFIX + "_entreprenours"
ENTERPRISE_ENTREPRENOURS_CATEGORY_URL_NAME = ENTERPRISE_PREFIX + "_entreprenours_category"
ENTERPRISE_ENTREPRENOURS_SUBCATEGORY_URL_NAME = ENTERPRISE_PREFIX + "_entreprenours_subcategory"
ENTERPRISE_ADD_PRODUCT_URL_NAME = ENTERPRISE_PREFIX + "_add_product"
ENTERPRISE_ADD_DISCOUNT_URL_NAME = ENTERPRISE_PREFIX + "_add_discount"
ENTERPRISE_SLUG_URL_KWARG = "slug_enterprise"

ENTERPRISE_CREATED = _("Subcategory created: {}")
ENTERPRISE_ALREADY_CREATED = _("Subcategory  already created: {}")


PRODUCT_PREFIX = "PRODUCT"

PRODUCT_VERBOSE_NAME = _("Product")
PRODUCT_VERBOSE_NAME_PLURAL = _("Product")

PRODUCT_LIST_URL_NAME = PRODUCT_PREFIX + conf.LIST_SUFFIX
PRODUCT_CREATE_URL_NAME = PRODUCT_PREFIX + conf.CREATE_SUFFIX
PRODUCT_DETAIL_URL_NAME = PRODUCT_PREFIX + conf.DETAIL_SUFFIX
PRODUCT_UPDATE_URL_NAME = PRODUCT_PREFIX + conf.UPDATE_SUFFIX
PRODUCT_DELETE_URL_NAME = PRODUCT_PREFIX + conf.DELETE_SUFFIX
DISCOUNTS_PREFIX = "DISCOUNTS"

DISCOUNTS_VERBOSE_NAME = _("Discounts")
DISCOUNTS_VERBOSE_NAME_PLURAL = _("Discounts")

DISCOUNTS_LIST_URL_NAME = DISCOUNTS_PREFIX + conf.LIST_SUFFIX
DISCOUNTS_CREATE_URL_NAME = DISCOUNTS_PREFIX + conf.CREATE_SUFFIX
DISCOUNTS_DETAIL_URL_NAME = DISCOUNTS_PREFIX + conf.DETAIL_SUFFIX
DISCOUNTS_UPDATE_URL_NAME = DISCOUNTS_PREFIX + conf.UPDATE_SUFFIX
DISCOUNTS_DELETE_URL_NAME = DISCOUNTS_PREFIX + conf.DELETE_SUFFIX
DISCOUNTS_QR_CODE_URL_NAME = DISCOUNTS_PREFIX + "_qr_code"

