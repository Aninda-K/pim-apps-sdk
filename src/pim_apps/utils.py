import os

os.environ['PIM_APP_BASE_URL']="https://pim-apps.unbxd.io/pim/"
os.environ['PIM_BASE_URL']="https://pim.unbxd.io/"
os.environ['A2C_BASE_URL']="https://api.api2cart.com/"
os.environ['PEPPERX_URL']="https://pim.unbxd.io/pepperx/"



def get_pim_app_domain():
    return os.environ['PIM_APP_BASE_URL']


def get_pim_domain():
    return os.environ['PIM_BASE_URL']


def get_a2c_domain():
    return os.environ['A2C_BASE_URL']


def get_pepperx_domain():
    return os.environ['PEPPERX_URL']