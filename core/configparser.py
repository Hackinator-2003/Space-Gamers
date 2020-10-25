from shutil import copyfile
import os
import logging

TYAPGE_CONF = {

}


def get_config(option="conf.ini",default="core/default.ini"):
    logging.debug("loading configuration="+str(option)+"and default="+str(default))

    assert os.path.isfile(default)
    if not os.path.isfile(option):copyfile(default, option)

    # charger les fichiers de configuration sous la forme d'un dict
    default_conf = get_config_dict(default)
    option_conf = get_config_dict(option)

    for section_name,section in default_conf.items():
        for key,value in default_conf[section_name].items():
            if key in option_conf[section_name].keys():default_conf[section_name][key] = option_conf[section_name][key]

    logging.debug("MERGED CONFIG "+str(default_conf))

    return default_conf



def get_config_dict(filePath):
    file_ = open(filePath,"r")
    returning = {}
    section = "global"
    returning["global"] = dict()
    for line in file_.readlines():
        line = line.strip()
        if line.startswith("#") or line == "": continue
        elif line == ":": section = "global";
        elif line.startswith(":"): section = line[1:]; returning[section] = dict()
        if "=" in line:
            value,key = line.split("=")
            returning[section][value.strip()] = key.strip()

    logging.debug("config for"+filePath+": "+str(returning))
    return returning





