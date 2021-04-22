import os
import number_quiz
import pronounciation_quiz
import gender_review
import plurals_review
import edit_voca

vocas_path = './vocas'
vocabulary_book = {}
voca_list = []
selected_voca = {}

def select_voca():

    print('----------------------------------------------')
    print('please select vocabulary packs you want to study. type the indexes and press enter')
    for i in range(len(voca_list)):
        print("{} : {}".format(i, voca_list[i]))
    selected_indexes = list(map(int, input().split()))
    temp = []
    for idx in selected_indexes:
        temp.append(voca_list[idx])
    selected_vocas = {}
    for title in temp:
        selected_vocas.update(vocabulary_book[title])

    print("voca successfully selected")
    print('----------------------------------------------')

    return selected_vocas


def update_vocas_list():
    idx_count = 0
    voca_note_dict = {}
    vocas_list = {}
    contents_list = os.listdir(vocas_path)
    for content in contents_list:
        if '.txt' in content:
            voca_note_dict[idx_count] = content[:-4:]
            idx_count += 1

    for idx in range(idx_count):
        vocas = {}
        title = voca_note_dict[idx]
        f = open(vocas_path + '/' + title + '.txt', 'r',encoding='utf-8')
        while True:
            line = f.readline()
            if line == '~':
                break
            word_and_meaning = line.split(' : ')
            word = word_and_meaning[0]
            meaning = word_and_meaning[1][:-1:]
            vocas[word] = meaning
        vocas_list[title] = vocas



    print('The vocabularys successfully updated')
    print('----------------------------------------------')

    return vocas_list

def main_menu():

    global selected_voca

    print("Welcome to the " + '\033[97m' + "*" + '\033[94m' + "*" + '\033[91m' + "*" + '\033[97m' + " Russian" + '\033[94m' + " Learning" + '\033[91m' + " Helper" + '\033[97m' + " *" + '\033[94m' + "*" + '\033[91m' +"*" + '\033[0m' "!!")
    print("This program is based on the lecture of 'Tanya's Russian Class' and originated by Hojin Cho, University Of Seoul.\nThe last update(v.1.0) was 2021.04.21")
    print('----------------------------------------------')
    _ = input('press any key to start')

    while 1:
        print('----------------------------------------------')
        print("Please select the course you want to study")
        print('0 = number_quiz')
        print('1 = pronounciation_quiz')
        print('2 = gender_quiz')
        print('3 = plurals_quiz')
        print('4 = edit_voca')
        print('voca = load_voca_list')
        print('select = Update words list to study')
        print('quit = exit\n')

        select_course = input()
        if select_course == '0':
            number_quiz.number_quiz()
            _ = input('press any key to back to main menu')
        if select_course == '1':
            pronounciation_quiz.alphabet_pronounciation_quiz()
            _ = input('press any key to back to main menu')
        if select_course == '2':
            gender_review.gender_review(selected_voca)
            _ = input('press any key to back to main menu')
        if select_course == '3':
            plurals_review.plural_review(selected_voca)
            _ = input('press any key to back to main menu')
        if select_course == '4':
            edit_voca()
            _ = input('press any key to back to main menu')
        if select_course == 'voca':
            for i in range(len(voca_list)):
                print("{} : {}".format(i, voca_list[i]))
                _ = input('press any key to back to main menu')
        if select_course == 'select':
            selected_voca = select_voca()
            _ = input('press any key to back to main menu')
        if select_course == 'quit':
            _ = input("You want to quit? y/n : ")
            if _ == 'y':
                break
            _ = input('press any key to back to main menu')

    return 0

if __name__ == "__main__":
    vocabulary_book = update_vocas_list()
    voca_list = list(vocabulary_book.keys())
    _ = input('press any key to start')
    selected_voca = select_voca()
    print(selected_voca)
    main_menu()