import os
import unicodedata

from django.contrib.auth.models import Group
from django.core.files import File


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
        username, password = self.generate_username_and_password(name)

        user, created = core_models.User.objects.get_or_create(
            username=username
        )

        if created:
            print(core_conf.USER_CREATED.format(username))
            user.set_password(password)
            user.save()
        else:
            print(core_conf.USER_ALREADY_CREATED.format(username))
        enterprise_manager_group = Group.objects.get(name=core_conf.ENTERPRISE_MANAGER_GROUP_NAME)
        user.groups.add(enterprise_manager_group)
        return user

    def generate_username_and_password(self, name):
        tokens = name.split()
        print(len(tokens))
        if 0 < len(tokens) < 3:
            username = "-".join(tokens).lower()
        else:
            username = f"{tokens[0]}-{tokens[2]}".lower()

        password = "-".join(tokens).lower()
        return username, password


    def create_file_with_users_and_passwords(self, all_data_file, output_file_name):
        """
from applications.core.controllers import load_data
data_loader = load_data.LoadData()
data_loader.create_file_with_users_and_passwords("applications/core/fixtures/info.csv", "applications/core/fixtures/username_and_passwords.csv")
        :param all_data_file:
        :param output_file_name:
        :return:
        """
        all_data = core_utils.read_data(all_data_file)
        print(output_file_name)
        output_file = open(output_file_name, "w+")
        output_file.write("emprendimiento,username,password\n")
        for line in all_data[1:]:
            username, password = self.generate_username_and_password(line[2])
            output_file.write(f"{line[1]},{username},{password}\n")

        output_file.close()

    def load_products(self, product_folder):
        """
from applications.core.controllers import load_data
data_loader = load_data.LoadData()
data_loader.load_products("../pictures")
        :param all_data_file:
        :param product_folder:
        :return:
        """
        for dir in os.listdir(product_folder):
            dir = unicodedata.normalize('NFC', dir)
            try:
                enterprise = core_models.Enterprise.objects.get(name=dir)
            except core_models.Enterprise.DoesNotExist:
                print(dir, "Does not exits")
                enterprise = None
            if enterprise is not None:
                for image in os.listdir(os.path.join(product_folder, dir)):
                    print(enterprise, os.path.join(product_folder, dir, image))
                    product = core_models.Product(
                        enterprise=enterprise,
                        name=image
                    )
                    product.picture.save(image, File(open(os.path.join(product_folder, dir, image), "rb")))
                    product.save()

    def load_social_media(self, fb_data):
        """
from applications.core.controllers import load_data
data_loader = load_data.LoadData()
data_loader.load_social_media("applications/core/fixtures/fb.csv")
        :param fb_data:
        :return:
        """
        all_data = core_utils.read_data(fb_data)
        for row in all_data:
            enterprise = None
            enterprise_name = row[1]
            try:
                enterprise = core_models.Enterprise.objects.get(name=enterprise_name)
            except core_models.Enterprise.DoesNotExist:
                print(enterprise_name, "Does not exits")
            if enterprise is not None:
                fb = row[4]
                instagram = row[5]
                if fb != "NO":
                    print(enterprise, fb)
                    enterprise.facebook_url = fb
                    enterprise.save()
                if instagram != "NO":
                    print(enterprise, instagram)
                    enterprise.instagram_url = instagram
                    enterprise.save()
