import os
import shutil


def get_one_line_info(line=""):
    line = line.strip()
    if (len(line) == 0):
        return None

    info_list = line.split(' ')[1:]

    return info_list


def extract_class(classline=""):
    info_list = get_one_line_info(classline)
    if (info_list == None):
        return None
    return info_list[0]


def get_class_dic(info_seq=0):
    class_dic = {}

    with open("./factory/classinfo/info" + str(info_seq) + ".txt", 'r') as f:
        lines = f.readlines()
        for j in range(len(lines)):
            if (j % 3 == 0):
                classname = extract_class(lines[j])
                if (classname == None):
                    break
                attr = get_one_line_info((lines[j + 1]))
                op = get_one_line_info(lines[j + 2])
                class_dic[classname] = {}
                class_dic[classname]["attr"] = attr
                class_dic[classname]["op"] = op

    return class_dic


if __name__ == "__main__":
    class_dic = get_class_dic()
    print(class_dic)
