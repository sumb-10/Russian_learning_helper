import os

vocas_path = './voca_main.py'

def check_vocas_list():
    voca_title_dict = {}
    contents_list = os.listdir(vocas_path)
    print(contents_list)
    idx = 0

    for content in contents_list:
        if content[-4:] == '.txt':
            voca_title_dict[idx] = content[:-4:]
            idx += 1

    print('list of voca = {}'.format(voca_title_dict))
    idx_end = idx + 1
    idx = 0

    f = open('./voca_main.py', 'w')
    for idx in range(idx_end):
        vocas = {}
        f = open(vocas_path + '/' + voca_title_dict[idx] + '.txt', 'r')
        while 1:
            if not word : break
            word = f.readline()
            meaning = f.readline()
            vocas[word] = meaning
        f.close()






check_vocas_list()

