import os

vocas_path = './vocas'

def update_vocas_list():
    idx_count = 0
    voca_note_dict = {}
    vocas_list = {}
    contents_list = os.listdir(vocas_path)
    for content in contents_list:
        if '.txt' in content:
            voca_note_dict[idx_count] = content[:-4:]
            idx_count += 1
    print(voca_note_dict)

    for idx in range(idx_count):
        print(idx)
        vocas = {}
        title = voca_note_dict[idx]
        f = open(vocas_path + '/' + title + '.txt', 'r')
        while True:
            line = f.readline()
            if not line:
                break
            word_and_meaning = line.split(' : ')
            word = word_and_meaning[0]
            meaning = word_and_meaning[1]
            vocas[word] = meaning
        vocas_list[title] = vocas

    print(vocas_list)

    return 0