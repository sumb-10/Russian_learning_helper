import fileinput
import sys

vocas_path = './voca_main.py'

def check_vocas_list():
    f = open('./voca_main.py', 'r')
    while 1:
        line = f.readline()
        if not line : break
        print(line)
    f.close()






check_vocas_list()

