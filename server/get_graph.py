import os

import matplotlib.pyplot as plt
import numpy as npy

from time_holder import time_holder


def get_holder_list():
    holder_list = []
    dirnames = os.listdir("./lib")
    for dirname in dirnames:
        tmp_holder = time_holder(dirname)
        tmp_holder.get_case_time()
        holder_list.append(tmp_holder)
    return holder_list
    # for holder in holder_list:
    #     print(holder.time_list)


def get_min_time_list(holder_list=[]):
    min_time_list = []
    for time_seq in range(len(holder_list[0].time_list)):
        tmp_min = 10101
        for holder in range(len(holder_list)):
            tmp_min = min(tmp_min, holder_list[holder].time_list[time_seq])
        min_time_list.append(tmp_min)
    return min_time_list


def get_mvp_cnt(holder_list=[], min_time_list=[]):
    for holder in holder_list:
        for time_seq in range(len(min_time_list)):
            if (abs(holder.time_list[time_seq] - min_time_list[time_seq]) <
                    0.00001):
                holder.mvp_cnt += 1
        # print(holder.dirname,holder.mvp_cnt)


def get_line_chart(holder_list=[]):
    plt.figure(figsize=(25, 10))
    plt.title('Time Used for All Simulators')
    plt.xlabel('testcase')
    plt.ylabel('time')

    x = [i for i in range(len(holder_list[0].time_list))]

    for holder in holder_list:
        plt.plot(x, holder.time_list, label=holder.dirname)

    plt.legend()
    plt.xticks(npy.arange(-1, len(x) + 1, 1))
    plt.savefig("./summary/graph/line.png")


def get_mvp_chart(holder_list):
    plt.figure(figsize=(30, 15))
    plt.title('MVP Count for All Simulators')
    plt.xlabel('Scheduler')
    plt.ylabel('MVP Count')

    dirnames = [holder.dirname for holder in holder_list]
    mvp_list = [holder.mvp_cnt for holder in holder_list]
    plt.bar(range(len(mvp_list)), mvp_list, tick_label=dirnames)

    plt.savefig("./summary/graph/mvp_bar.png")


def get_stats_chart(holder_list=[]):
    for holder in holder_list:
        holder.get_stats()

    plt.figure(figsize=(30, 15))
    plt.title('Statistics for All Simulators')
    plt.xlabel('Simulator')
    plt.ylabel('Statistics')

    dirnames = [holder.dirname for holder in holder_list]
    mean_list = [holder.mean * 1000 for holder in holder_list]
    # var_list = [0 for holder in holder_list]
    std_list = [holder.std * 1000 for holder in holder_list]
    x = npy.arange(len(dirnames))
    rects1 = plt.bar(x,
                     mean_list,
                     width=0.8 / 2,
                     tick_label=dirnames,
                     label='mean')
    rects2 = plt.bar(x + 0.8 / 2, std_list, width=0.8 / 2, label='std')
    plt.legend()

    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2,
                 height + 1,
                 str(height)[:9],
                 ha="center",
                 va="bottom")
    for rect in rects2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2,
                 height + 1,
                 str(height)[:9],
                 ha="center",
                 va="bottom")

    plt.savefig("./summary/graph/stats_bar.png")


def get_graph():
    holder_list = get_holder_list()
    min_time_list = get_min_time_list(holder_list)
    get_mvp_cnt(holder_list, min_time_list)
    get_line_chart(holder_list)
    get_mvp_chart(holder_list)
    get_stats_chart(holder_list)


if __name__ == "__main__":
    get_graph()
