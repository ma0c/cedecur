from applications.core import (
    conf as core_conf,
    models as core_models,
    utils as core_utils
)


class LoadData(object):

    def get_category_and_created_from_name(self, category):
        return core_models.Category.objects.get_or_create(
                name=category.strip().capitalize()
            )
    def get_subcategory_and_created_from_name(self, subcategory):
        return core_models.Subcategory.objects.get_or_create(
                name=subcategory.strip().capitalize()
            )
    def load_categories(self, categories_file):
        """
from applications.core.controllers import load_data
data_loader = load_data.LoadData()
data_loader.load_categories("applications/core/fixtures/categories.txt")
        :param categories_file:
        :return:
        """
        categories = open(categories_file).readlines()
        for category in categories:
            category_object, created = self.get_category_and_created_from_name(category)
            if created:
                print(core_conf.CATEGORY_CREATED.format(category))
            else:
                print(core_conf.CATEGORY_ALREADY_CREATED.format(category))

    def load_subcategories(self, subcategories_file):
        """
from applications.core.controllers import load_data
data_loader = load_data.LoadData()
data_loader.load_subcategories("applications/core/fixtures/subcategories.txt")
        :param
        categories_file:
        :return:
        """
        subcategories = open(subcategories_file).readlines()
        for subcategory in subcategories:
            subcategory_object, created = self.get_subcategory_and_created_from_name(subcategory)
            if created:
                print(core_conf.SUBCATEGORY_CREATED.format(subcategory))
            else:
                print(core_conf.SUBCATEGORY_ALREADY_CREATED.format(subcategory))

    def attach_categories_to_subcategories(self, categories_attached_file):
        """
from applications.core.controllers import load_data
data_loader = load_data.LoadData()
data_loader.attach_categories_to_subcategories("applications/core/fixtures/categories_attached.txt")
        :param categories_attached_file:
        :return:
        """
        categories_attached = open(categories_attached_file).readlines()
        for category_attached in categories_attached:
            category_name, *subcategory_name = category_attached.split("-")
            category, _ = self.get_category_and_created_from_name(category_name)
            subcategory, _ = self.get_subcategory_and_created_from_name("-".join(subcategory_name).strip().capitalize())
            subcategory.category = category
            subcategory.save()

    def create_enterprises(self, all_data_file):
        """
from applications.core.controllers import load_data
data_loader = load_data.LoadData()
data_loader.create_enterprises("applications/core/fixtures/info.csv")
        :param all_data_file:
        :return:
        """
        all_data = core_utils.read_data(all_data_file)

        for line in all_data[1:]:
            user = self.create_user_from_name(line[2])
            category, _ = self.get_category_and_created_from_name(line[3])
            subcategory, _ = self.get_subcategory_and_created_from_name(line[4])
            enterprise, created = core_models.Enterprise.objects.get_or_create(
                name=line[1]
            )
            if created:
                print(core_conf.ENTERPRISE_CREATED.format(subcategory))
                enterprise.owner = user
                enterprise.category = category
                enterprise.sub_category = subcategory
                enterprise.save()
            else:
                print(core_conf.ENTERPRISE_ALREADY_CREATED.format(subcategory))

    def create_user_from_name(self, name):
        tokens = name.split()
        print(len(tokens))
        if 0 < len(tokens) < 3:
            username = "-".join(tokens).lower()
        else:
            username = f"{tokens[0]}-{tokens[2]}".lower()

        user, created = core_models.User.objects.get_or_create(
            username=username
        )

        if created:
            print(core_conf.USER_CREATED.format(username))
            user.set_password("-".join(tokens).lower())
            user.save()
        else:
            print(core_conf.USER_ALREADY_CREATED.format(username))
        return user
