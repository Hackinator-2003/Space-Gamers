# By Cypooos
from shutil import copyfile
import os

def get_config(option="conf.ini",default="core/default.ini"):
    assert os.path.isfile(default)
    if not os.path.isfile(option):copyfile(default, option)
    default_conf = get_config_dict(default)
    option_conf = get_config_dict(option)
    for key,value in option_conf.items():
        if key in default_conf.keys():default_conf[key] = value



def get_config_dict(file_):
    return None





