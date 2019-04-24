import csv
import qrcode
import base64
from io import BytesIO


def save_iterable_to_a_file(iterable, filename):
    f = open(filename, "w+")
    [f.write(f"{x}\n") for x in iterable]
    f.close()


def read_data(file_name):
    """
from applications.core.utils import read_data
read_data("fixtures/info.csv")
    :param file_name:
    :return:
    """
    info_file = open(file_name)
    reader = csv.reader(info_file)
    all_rows = list()
    for r in reader:
        all_rows.append(r)

    return all_rows


def extract_categories(file_name):
    """
from applications.core.utils import extract_categories
extract_categories("fixtures/info.csv")
    :param file_name:
    :return:
    """
    all_rows = read_data(file_name)
    categories = {r[3].lower() for r in all_rows}
    subcategories = {r[4].lower() for r in all_rows}
    categories_attached = {f"{r[3].lower()} - {r[4].lower()}" for r in all_rows}
    save_iterable_to_a_file(categories, "fixtures/categories.txt")
    save_iterable_to_a_file(subcategories, "fixtures/subcategories.txt")
    save_iterable_to_a_file(categories_attached, "fixtures/categories_attached.txt")


def get_base64_qr_code(data):
    qr_image = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_image.add_data(data)
    qr_image.make(fit=True)

    img = qr_image.make_image()

    buffered_image = BytesIO()
    img.save(buffered_image, format="JPEG")
    return base64.b64encode(buffered_image.getvalue()).decode()