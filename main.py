import json


def recursive_type_string(dict):
    if len(dict["args"]) == 0:
        return dict["name"]
    elif len(dict["args"]) == 1:
        return dict["name"] + "<" + recursive_type_string(dict["args"][0]["type"]) + ">"
    else:
        typestring = dict["name"] + "<"
        for i, subtype in enumerate(dict["args"]):
            typestring += recursive_type_string(subtype["type"])
            if i != len(dict["args"]) - 1:
                typestring += ","
        typestring += ">"
        return typestring


json_name = ["data.json"]

dependencies = []

for file in json_name:
    data = open("data.json")

    file_dict = json.load(data)

    classname = file_dict["name"]

    interface_list = []

    fields = []

    methods = []

    if "interfaces" in file_dict:
        interface_list = file_dict["interfaces"]

    if "fields" in file_dict:
        for member in file_dict["fields"]:
            fields.append(
                {"name": member["name"], "type": recursive_type_string(member["type"])})

    if "methods" in file_dict:
        for method in file_dict["methods"]:
            pass
