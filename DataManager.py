import os
import Esentiale

debug = False
printerName = "PollVote"

mypath = os.path.dirname(os.path.realpath(__file__)) + "\\"
proxies = []


def load_data():
    load_list("proxy.txt", proxies, True)
    # load_files_list("crop",names)


def load_list(path, my_list, removable=False):
    printX("load_list")
    if (path.count(":\\") == 0):
        path = mypath + path
    my_list.clear()
    if (removable == False):
        my_list.append("1")
    else:
        my_list.append("REMOVABLE|" + path)

    if (os.path.exists(path) == False):
        print("FATAL ERROR LOAD_LIST")
        exit(692)
    with open(path) as f:
        for line in f:
            if (len(line.replace("\n", "")) > 0): my_list.append(line.replace("\n", ""))
    Esentiale.shuffle_list_without_first(my_list)
    if (len(my_list) == 1):
        print("FATAL ERROR LOAD_LIST 2")
        exit(693)


def load_files_list(path, my_list):
    printX("load_files_list")
    if (path.count(":\\") == 0):
        path = mypath + path
    my_list.clear()
    my_list.append("1")

    if (os.path.exists(path) == False):
        print("FATAL ERROR LOAD_LIST 3")
        exit(694)
    for file in os.listdir(path):
        filename = os.fsdecode(file)
        if (filename.count(".jpg") or filename.count(".png")):
            my_list.append(mypath + filename)
    Esentiale.shuffle_list_without_first(my_list)
    if (len(my_list) == 1):
        print("FATAL ERROR LOAD_LIST 4")
        exit(695)


def get_next_item(my_list):
    if (my_list[0].count("|")):
        return get_next_item_removable(my_list)
    printX("Get_next_item")
    index = int(my_list[0])
    if index > len(my_list) - 1:
        index = 1
    to_return = my_list[index]
    my_list[0] = str(index + 1)
    return to_return


def get_next_item_removable(my_list):
    printX("Get_next_item_removable")
    path = my_list[0].split("|")[1]
    to_return = str(my_list[1])
    del my_list[1]
    file_output = ""
    for i in range(1, len(my_list)):
        file_output += my_list[i] + "\n"
    f = open(path, "w")
    f.write(file_output)
    f.close()
    return to_return


def get_proxy():
    return get_next_item(proxies)


def printX(txt):
    if debug:
        print("[", printerName, "]  ", txt)
