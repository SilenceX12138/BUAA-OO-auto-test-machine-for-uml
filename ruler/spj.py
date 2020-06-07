import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "./ruler")


# valid strip CRLF information list
def get_list(filename):
    result_list = []
    with open(filename, 'r') as f:
        tmp_list = f.readlines()
        for tmp in tmp_list:
            tmp = tmp.strip('\n')
            if (len(tmp) == 0 or tmp.find("time") != -1):
                continue
            result_list.append(tmp)
    return result_list


# check time limit
def time_judge(output_file):
    with open(output_file, 'r') as f_out:
        last_move = f_out.readlines()[0]
        pos = last_move.index(':')
        time = (float)(last_move[pos + 2:])
        if (time >= 2.00 - 0.000001):
            return True
    return False


def sort_and_cmp(output1="", output2=""):
    pos1 = output1.index('(')
    pos2 = output1.index(')')
    list1 = output1[pos1 + 1:pos2].split(',')
    pos1 = output2.index('(')
    pos2 = output2.index(')')
    list2 = output2[pos1 + 1:pos2].split(',')
    list1.sort()
    list2.sort()
    return not (list1 == list2)


def cmp_judge(data_file, output_file, template_file):
    input_list = get_list(data_file)
    output_list = get_list(output_file)
    template_list = get_list(template_file)

    # filter length difference
    # if (len(input_list) != len(output_list)
    #         or len(input_list) != len(template_list)):
    #     return "request length has problem"

    # check time
    if (time_judge(output_file)):
        return "time is longer than expected"

    # check correction
    for i in range(len(template_list)):
        if (output_list[i].find('(') != -1):
            r = sort_and_cmp(output_list[i], template_list[i])
            if (r):
                return "line " + str(
                    i + 1) + " has problem with request: " + input_list[i]
        elif (output_list[i].find("operation visibility") != -1):
            output_list[i] = output_list[i].replace(' ', '')
            template_list[i] = template_list[i].replace(' ', '')
            r = (output_list[i] != template_list[i])
            if (r):
                return "line " + str(
                    i + 1) + " has problem with request: " + input_list[i]
        elif (output_list[i] != template_list[i]):
            return "line " + str(
                i + 1) + " has problem with request: " + input_list[i]

    return ""


def check(data_file, output_file, template_file):
    r = cmp_judge(data_file, output_file, template_file)
    if (len(r) != 0):
        return "cmp_judge: " + r + "\n"
    return ""


if __name__ == "__main__":
    # for i in range(10):
    #     r = check("./data/testcase" + str(i) + ".txt",
    #               "./output/saber/output" + str(i) + ".txt",
    #               "./template/template4.txt")
    #     print(i, r)
    r = check("./data/testcase0.txt", "./output/general/output6.txt",
              "./template/template6.txt")
    print(r)
