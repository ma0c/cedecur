from applications.core.controllers import load_data


def setup():
    data_loader = load_data.LoadData()
    data_loader.load_categories("applications/core/fixtures/categories.txt")
    data_loader.load_subcategories("applications/core/fixtures/subcategories.txt")
    data_loader.attach_categories_to_subcategories("applications/core/fixtures/categories_attached.txt")
    data_loader.create_enterprises("applications/core/fixtures/info.csv")
