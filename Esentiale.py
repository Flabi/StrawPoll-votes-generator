import random
import os
import string

import spintax  # pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org spintax


debug = False
printerName = "PollVote"
app_name = "PollVote"
AppFolder = os.environ['USERPROFILE'] + "\\Documents\\" + app_name + " Reports\\"
mypath = os.path.dirname(os.path.realpath(__file__)) + "\\"

def add_report(txt, name):
    printX("Adding report " + name + ", Text len: " + str(len(txt)))
    try:
        global AppFolder
        if (os.path.exists(AppFolder) == False):
            os.mkdir(AppFolder)
        fileName = name + str(random_nr(10000, 99999)) + ".txt"
        f = open(AppFolder + fileName, "w",encoding="utf-8")
        f.write(txt)
        f.close()
    except Exception as e:
        printX("ERROR: " + str(e))


def random_nr(nr1, nr2):
    my_nr = random.randrange(nr1, nr2 + 1)
    printX("Random nr generated: " + str(my_nr))
    return my_nr


def spin(txt):
    rez = spintax.spin(txt)
    printX("Text spintax result:" + rez)
    return rez


def shuffle_list(list):
    printX("List shuffle")
    random.shuffle(list)

def shuffle_list_without_first(list):
    printX("List shuffle without first")
    copy=list[1:]
    random.shuffle(copy)
    list[1:]=copy

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    mystr = ''.join(random.choice(letters) for i in range(stringLength))
    printX("RandomString generated: " + mystr)
    return mystr

def save_to_file(content, title):
    try:
        f = open(mypath + title, "w",encoding="utf-8")
        f.write(content)
        f.close()
    except:
        print("ERROR SAVING FILE TO " + title)

def get_from_file(title):
    try:
        f = open(mypath + title, "r",encoding="utf-8")
        to_return=f.readlines()
        f.close()
        return to_return
    except:
        print("ERROR SAVING FILE TO " + title)

def printX(txt):
    if debug:
        print("[", printerName, "]  ", txt)
