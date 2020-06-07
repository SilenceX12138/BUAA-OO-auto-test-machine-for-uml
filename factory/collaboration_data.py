import os

one_interaction_ins_list = ["PTCP_OBJ_COUNT", "MESSAGE_COUNT"]
two_interaction_ins_list = ["INCOMING_MSG_COUNT"]


def get_one_interaction_data(state_machine_name=""):
    one_interaction_data = []

    for one_interaction_ins in one_interaction_ins_list:
        data = one_interaction_ins + " " + state_machine_name
        one_interaction_data.append(data)

    return one_interaction_data


def get_two_state_data(interaction_name_list=[], lifeline_name_list=[]):
    two_interaction_data = []

    for two_interaction_ins in two_interaction_ins_list:
        for interaction in interaction_name_list:
            for lifeline in lifeline_name_list:
                data = two_interaction_ins + " " + interaction + " " + lifeline
                two_interaction_data.append(data)

    return two_interaction_data


def get_collaboration_info(info_seq=0):
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
            "java -jar ./factory/collaboration-info-extractor.jar < ./factory/umlinfo/umlinfo"
            + str(i) + ".txt > ./factory/collaborationinfo/info" + str(i) +
            ".txt")
        i += 1


def get_collaboration_pedia(info_seq=0):
    interaction_name_list = []
    lifeline_name_list = []

    with open("./factory/collaborationinfo/info" + str(info_seq) + ".txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            if (line.find("interaction") != -1):
                interaction_name_list.append(line.split()[-1])
            else:
                lifeline_name_list.append(line.split()[-1])

    return interaction_name_list, lifeline_name_list


def gene_collaboration_data(interaction_name_list=[], lifeline_name_list=[]):
    collaboration_data = []

    for interaction in interaction_name_list:
        collaboration_data.extend(get_one_interaction_data(interaction))

    collaboration_data.extend(
        get_two_state_data(interaction_name_list, lifeline_name_list))

    return collaboration_data


def get_collaboration_data(info_seq=0):
    interaction_name_list, lifeline_name_list = get_collaboration_pedia(
        info_seq)
    collaboration_data = gene_collaboration_data(interaction_name_list,
                                                 lifeline_name_list)
    return collaboration_data


if __name__ == "__main__":
    print(get_collaboration_data(0))
