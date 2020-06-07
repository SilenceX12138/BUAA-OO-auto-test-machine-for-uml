import os

one_state_machine_ins_list = [
    # "STATE_COUNT",
    "TRANSITION_COUNT"
]
two_state_ins_list = ["SUBSEQUENT_STATE_COUNT"]


def get_one_state_machine_data(state_machine_name=""):
    one_state_machine_data = []

    for one_state_machine_ins in one_state_machine_ins_list:
        data = one_state_machine_ins + " " + state_machine_name
        one_state_machine_data.append(data)

    return one_state_machine_data


def get_two_state_data(state_machine_name_list=[], state_name_list=[]):
    two_state_data = []

    for two_state_ins in two_state_ins_list:
        for state_machine in state_machine_name_list:
            for state in state_name_list:
                data = two_state_ins + " " + state_machine + " " + state
                two_state_data.append(data)

    return two_state_data


def get_state_info(info_seq=0):
    uml_files = []
    uml_files = os.listdir("./factory/uml")
    i = 0
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
            "java -jar ./factory/state-info-extractor.jar < ./factory/umlinfo/umlinfo"
            + str(i) + ".txt > ./factory/stateinfo/info" + str(i) + ".txt")
        i += 1


def get_state_pedia(info_seq=0):
    state_machine_name_list = []
    state_name_list = []

    with open("./factory/stateinfo/info" + str(info_seq) + ".txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            if (line.find("machine") != -1):
                state_machine_name_list.append(line.split()[-1])
            else:
                state_name_list.append(line.split()[-1])

    return state_machine_name_list, state_name_list


def gene_state_data(state_machine_name_list=[], state_name_list=[]):
    state_data = []

    for state_machine in state_machine_name_list:
        state_data.extend(get_one_state_machine_data(state_machine))

    state_data.extend(
        get_two_state_data(state_machine_name_list, state_name_list))

    return state_data


def get_state_data(info_seq=0):
    get_state_info(info_seq)
    state_machine_name_list, state_name_list = get_state_pedia(info_seq)
    state_data = gene_state_data(state_machine_name_list, state_name_list)
    return state_data


if __name__ == "__main__":
    print(get_state_data(0))
