import itertools

arrangement_ins_list = ["CLASS_ATTR_COUNT", "CLASS_OPERATION_COUNT"]

attr_modes = ["ALL", "SELF_ONLY"]
op_modes = ["NON_RETURN", "RETURN", "NON_PARAM", "PARAM"]


def get_mode_data(ins="", classname="", mode_list=[], mode_count=1):
    mode_data = []

    mode_permutation_list = list(itertools.permutations(mode_list, mode_count))
    for mode_permutation in mode_permutation_list:
        data = ins + " " + classname
        for mode in mode_permutation:
            data += " " + mode
        mode_data.append(data)

    return mode_data


def get_one_class_data(classname="", mode=0, mode_count=1):
    one_class_data = []
    ins = ""
    mode_list = []
    if (mode == 0):  # 0 mode is for attr
        ins = arrangement_ins_list[0]
        mode_list = attr_modes
    elif (mode == 1):  # 1 mode is for op
        ins = arrangement_ins_list[1]
        mode_list = op_modes

    one_class_data = get_mode_data(ins, classname, mode_list, mode_count)
    return one_class_data


def get_arrangement_data(classname_list=[]):
    arrangement_data = []

    for classname in classname_list:
        # only one mode for attr
        arrangement_data.extend(get_one_class_data(classname, 0, 1))
        # five mode for op
        # arrangement_data.extend(get_one_class_data(classname, 1, 0))
        arrangement_data.extend(get_one_class_data(classname, 1, 1))
        # arrangement_data.extend(get_one_class_data(classname, 1, 2))
        # arrangement_data.extend(get_one_class_data(classname, 1, 3))
        # arrangement_data.extend(get_one_class_data(classname, 1, 4))

    return arrangement_data


if __name__ == "__main__":
    arrangement_data = get_arrangement_data(["Alice", "Bob"])
    for data in arrangement_data:
        print(data)
