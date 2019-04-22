from base import setup as setup_base

from applications.core.controllers import load_data

from applications.core import (
    conf as core_conf
)


def setup():
    setup_base.configure_groups_and_permissions(
        core_conf.GROUPS,
        core_conf.PERMISSIONS
    )
    data_loader = load_data.LoadData()
    data_loader.load_categories("applications/core/fixtures/categories.txt")
    data_loader.load_subcategories("applications/core/fixtures/subcategories.txt")
    data_loader.attach_categories_to_subcategories("applications/core/fixtures/categories_attached.txt")
    data_loader.create_enterprises("applications/core/fixtures/info.csv")
