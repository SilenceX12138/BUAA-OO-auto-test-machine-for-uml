import os
import random
import shutil
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "./factory")

from arrangement_data import get_arrangement_data
from class_extractor import get_class_dic
from collaboration_data import get_collaboration_data, get_collaboration_info
from name_data import get_name_data
from single_data import get_single_data
from state_data import get_state_data, get_state_info
from traverse_data import get_traverse_data


def get_info():
    uml_files = []
    uml_files = os.listdir("./factory/uml")
    i = 0
    if (os.path.exists("./factory/classinfo")):
        shutil.rmtree("./factory/classinfo")
    if (os.path.exists("./factory/umlinfo")):
        shutil.rmtree("./factory/umlinfo")
    os.mkdir("./factory/classinfo")
    os.mkdir("./factory/umlinfo")
    for uml_file in uml_files:
        os.system(
            "java -jar ./factory/uml-homework.jar dump -s ./factory/uml/" +
            uml_file + " -n Model -t UMLModel > ./factory/umlinfo/umlinfo" +
            str(i) + ".txt")
        lines = []
        with open("./factory/umlinfo/umlinfo" + str(i) + ".txt", "r") as f:
            lines = f.readlines()
        lines.append("END_OF_MODEL\n")
        with open("./factory/umlinfo/umlinfo" + str(i) + ".txt", "w") as f:
            f.writelines(lines)
        os.system(
            "java -jar ./factory/class-info-extractor.jar < ./factory/umlinfo/umlinfo"
            + str(i) + ".txt > ./factory/classinfo/info" + str(i) + ".txt")
        i += 1


def get_class_data(class_dic={}, count=10, info_seq=0):
    class_data = []
    normal_data = []
    interfere_data = []

    classname_list = class_dic.keys()

    arrangement_data = get_arrangement_data(classname_list)
    name_data = get_name_data(classname_list)
    single_data = get_single_data()
    traverse_data = get_traverse_data(class_dic)

    normal_data = arrangement_data + name_data + single_data + traverse_data
    class_data = normal_data + interfere_data
    random.shuffle(class_data)

    return class_data


def gene_data(case_count=10):
    if (os.path.exists("./data")):
        shutil.rmtree("./data")
        shutil.rmtree("./factory/classinfo")
        shutil.rmtree("./factory/stateinfo")
        shutil.rmtree("./factory/collaborationinfo")
    os.mkdir("./data")
    os.mkdir("./factory/classinfo")
    os.mkdir("./factory/stateinfo")
    os.mkdir("./factory/collaborationinfo")
    get_info()
    total_count = 0
    info_count = max(len(os.listdir("./factory/uml")),
                     len(os.listdir("./factory/umlinfo")))
    per_case_count = case_count // info_count + 1
    for i in range(info_count):
        class_dic = get_class_dic(info_seq=i)
        get_state_info(info_seq=i)
        get_collaboration_info(info_seq=i)
        for j in range(per_case_count):
            with open("./data/testcase" + str(total_count) + ".txt", 'w') as f:
                with open("./factory/umlinfo/umlinfo" + str(i) + ".txt",
                          "r") as f_info:
                    builder_data = f_info.readlines()
                f.writelines(builder_data)
                data_list = []
                data_list.extend(
                    get_class_data(class_dic=class_dic, info_seq=i))
                data_list.extend(get_state_data(info_seq=i))
                data_list.extend(get_collaboration_data(info_seq=i))
                for data in data_list:
                    f.writelines(data + "\n")
            total_count += 1


if __name__ == "__main__":
    gene_data()
    # get_info()
