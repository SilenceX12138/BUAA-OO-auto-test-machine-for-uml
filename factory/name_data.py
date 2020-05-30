name_ins_list = [
    "CLASS_TOP_BASE", "CLASS_INFO_HIDDEN", "CLASS_ASSO_COUNT",
    "CLASS_IMPLEMENT_INTERFACE_LIST", "CLASS_ASSO_CLASS_LIST"
]


def get_one_class_data(classname=""):
    one_class_data = []

    for name_ins in name_ins_list:
        data = name_ins + " " + classname
        one_class_data.append(data)
    
    return one_class_data

def get_name_data(classname_list = []):
    name_data = []

    for classname in classname_list:
        name_data.extend(get_one_class_data(classname))
    
    return name_data

if __name__ == "__main__":
    print(get_name_data(["Alice","Bob"]))
