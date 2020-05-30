traverse_ins_set = ["CLASS_ATTR_VISIBILITY", "CLASS_OPERATION_VISIBILITY"]


def get_one_class_data(classname="", specified_class={}, mode=0):
    one_class_data = []
    traverse_ins = ""
    traverse_list = []
    if (mode == 0):  # 0 mode is for attr
        traverse_ins = traverse_ins_set[0]
        traverse_list = specified_class["attr"]
    elif (mode == 1):  # 1 mode is for op
        traverse_ins = traverse_ins_set[1]
        traverse_list = specified_class["op"]

    for name in traverse_list:
        data = traverse_ins + " " + classname + " " + name
        one_class_data.append(data)

    return one_class_data


def get_traverse_data(class_dic={}):
    traverse_data = []

    for classname in class_dic:
        traverse_data.extend(  # attr data 
            get_one_class_data(classname, class_dic[classname], 0))
        traverse_data.extend(  # op data
            get_one_class_data(classname, class_dic[classname], 1))

    return traverse_data


if __name__ == "__main__":
    class_dic = {
        "A": {
            "attr": ["a1", "a2"],
            "op": ["a3", "a4"]
        },
        "B": {
            "attr": ["b3", "b4"],
            "op": ["b1", "b2"]
        },
    }
    traverse_data = get_traverse_data(class_dic)
    for data in traverse_data:
        print(data)
