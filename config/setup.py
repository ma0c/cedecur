from applications.core.setup import setup as core_setup
from base import conf as base_conf


def setup():
    """
from config.setup import setup
setup()
    :return:
    """

    print(base_conf.CONFIGURING_APPLICATION.format("Core"))
    core_setup()
