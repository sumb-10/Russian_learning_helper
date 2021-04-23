import os
import sys
from colorama import init, Fore, Style
import number_quiz
import pronounciation_review
import gender_review
import plurals_review
import edit_voca

init()
normal_vocas_path = './vocas/normal_voca'
grammatical_vocas_path = './vocas/grammatical_voca'
normal_vocabulary_book = {}
grammer_vocabulary_book = {}
normal_voca_list = []
selected_voca = {}

big_letter = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
small_letter = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
russian_alphabet_dict = {big_letter[i] : small_letter[i] for i in range(len(big_letter))}


def make_all_letter_small(word):

    wordlen = len(word)
    new_word = ''
    for i in range(wordlen):
        if word[i] in russian_alphabet_dict:
            new_word += russian_alphabet_dict[word[i]]
        else:
            new_word += word[i]
    return new_word


def select_voca():

    print('----------------------------------------------')
    print('please select vocabulary packs you want to study. type the indexes and press enter')
    for i in range(len(normal_voca_list)):
        print("{} : {}".format(i, normal_voca_list[i]))
    try:
        selected_indexes = list(map(int, input("select packs : ").split()))
        temp = []
        for idx in selected_indexes:
            temp.append(normal_voca_list[idx])
        selected_vocas = {}
        for title in temp:
            selected_vocas.update(normal_vocabulary_book[title])

        print("voca successfully selected")
        print('----------------------------------------------')

        return selected_vocas
    except:
        print("Error occured, press anykey to retry",end='')
        _ = input('')
        return {}


def update_normal_vocas_list():

    idx_count = 0
    voca_note_dict = {}
    vocas_list = {}
    contents_list = os.listdir(normal_vocas_path)

    try:
        for content in contents_list:
            if '.txt' in content:
                voca_note_dict[idx_count] = content[:-4:]
                idx_count += 1

        for idx in range(idx_count):
            vocas = {}
            title = voca_note_dict[idx]
            f = open(normal_vocas_path + '/' + title + '.txt', 'r',encoding='utf-8')
            while True:
                line = f.readline()
                if line == '~':
                    break
                if not line:
                    print("Error occured, press anykey to quit the program.")
                    print("Please check the the file, '{}' in the 'vocas' directory if they are written properly.".format(title+".txt"))
                    _ = input('\n')
                    return {}
                word_and_meaning = line.split(' : ')
                word = word_and_meaning[0]
                meaning = word_and_meaning[1][:-1:]
                vocas[word] = meaning
            vocas_list[title] = vocas

        print('The vocabularys successfully updated')
        print('----------------------------------------------')

        return vocas_list

    except:
        print("Error occured, press anykey to quit the program.")
        print("Please check the the files in the 'vocas' directory if they are written properly.")
        _ = input('\n')
        return {}


def update_grammatical_vocas_list():

    idx_count = 0
    voca_note_dict = {}
    vocas_list = {}
    contents_list = os.listdir(grammatical_vocas_path)

    try:
        for content in contents_list:
            if '.txt' in content:
                voca_note_dict[idx_count] = content[:-4:]
                idx_count += 1

        for idx in range(idx_count):
            vocas = {}
            title = voca_note_dict[idx]
            f = open(grammatical_vocas_path + '/' + title + '.txt', 'r',encoding='utf-8')
            while True:
                line = f.readline()
                if line == '~':
                    break
                if not line:
                    print("Error occured, press anykey to quit the program.")
                    print("Please check the the file, '{}' in the 'vocas' directory if they are written properly.".format(title+".txt"))
                    _ = input('\n')
                    return {}
                word_and_meaning = line.split(' : ')
                word = word_and_meaning[0]
                meaning = word_and_meaning[1][:-1:]
                vocas[word] = meaning
            vocas_list[title] = vocas

        print('The vocabularys successfully updated')
        print('----------------------------------------------')

        return vocas_list

    except:
        print("Error occured, press anykey to quit the program.")
        print("Please check the the files in the 'vocas' directory if they are written properly.")
        _ = input('\n')
        return {}


def main_menu():

    global selected_voca

    print("Welcome to the " + Fore.WHITE + Style.BRIGHT + "*" + Fore.BLUE + Style.BRIGHT + "*" + Fore.RED + Style.BRIGHT + "*" + Fore.WHITE + Style.BRIGHT + " Russian" + Fore.BLUE + Style.BRIGHT + " Learning" + Fore.RED + Style.BRIGHT + " Helper" + Fore.BLUE + Style.BRIGHT + " *" + Fore.WHITE + Style.BRIGHT + "*" + Fore.RED + Style.BRIGHT + "*" + Style.RESET_ALL + "!!")
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
        print('quit = exit')

        select_course = input("select course : ")
        if select_course == '0':
            number_quiz.number_quiz()
            _ = input('press any key to back to main menu')
        if select_course == '1':
            pronounciation_review.pronounciation_review(selected_voca)
            _ = input('press any key to back to main menu')
        if select_course == '2':
            gender_review.gender_review(selected_voca, grammatical_vocabulary_book)
            _ = input('press any key to back to main menu')
        if select_course == '3':
            plurals_review.plural_review(selected_voca, grammatical_vocabulary_book)
            _ = input('press any key to back to main menu')
        if select_course == '4':
            edit_voca.edit_vocas()
            _ = input('press any key to back to main menu')
        if select_course == 'voca':
            for i in range(len(normal_voca_list)):
                print("{} : {}".format(i, normal_voca_list[i]))
                _ = input('press any key to back to main menu')
        if select_course == 'select':
            selected_voca = select_voca()
            _ = input('press any key to back to main menu')
        if select_course == 'quit':
            _ = input("You want to quit? y/n : ")
            if _ == 'y':
                break
            _ = input('press any key to back to main menu')
        else:
            print("You pressed wrong key. Please input correct command")
            _ = input('Press any key to retry')

    return 0


if __name__ == "__main__":
    normal_vocabulary_book = update_normal_vocas_list()
    if normal_vocabulary_book == {}:
        sys.exit()
    normal_voca_list = list(normal_vocabulary_book.keys())

    grammatical_vocabulary_book = update_grammatical_vocas_list()
    if grammatical_vocabulary_book == {}:
        sys.exit()

    _ = input('press any key to start')
    while selected_voca == {}:
        selected_voca = select_voca()
    main_menu()