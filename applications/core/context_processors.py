from applications.core import (
    models as core_models,
    conf as core_conf
)


def categories(request):
    return {
        "categories": core_models.Category.objects.filter(active=True),
        "category_filter_url_name": core_conf.ENTERPRISE_ENTREPRENOURS_CATEGORY_URL_NAME,
        "subcategory_filter_url_name": core_conf.ENTERPRISE_ENTREPRENOURS_SUBCATEGORY_URL_NAME
    }
