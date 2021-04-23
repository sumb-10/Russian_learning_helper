import random
from colorama import init, Fore, Style

init()
kiril_alphabet = {'Аа' : '/a/', 'Бб' : '/b/', 'Вв' : '/v/', 'Гг' : '/ɡ/', 'Дд' : '/d/', 'Ее' : '/je/', 'Ёё': '/jo/', 'Жж' : '/ʐ/', 'Зз' : '/z/', 'Ии' : '/i/, / ʲi/, or /ɨ/' , 'Йй' : '/j/', 'Кк' : '/k/ or /kʲ/', 'Лл' : '/ɫ/ or /lʲ/', 'Мм' : '/m/ or /mʲ/', 'Нн' : '/n/ or /nʲ/', 'Оо' : '/o/', 'Пп' : '/p/ or /pʲ/', 'Рр' : '/r/ or /rʲ/', 'Сс' : '/s/ or /sʲ/', 'Тт' : '/t/ or /tʲ/', 'Уу' : '/u/', 'Фф' : '/f/ or /fʲ/', 'Хх' : '/x/ or /xʲ/', 'Цц' : '/ts/', 'Чч' : '/tɕ/', 'Шш' : '/ʂ/', 'Щщ' : '/ɕː/, /ɕ/', 'Ъъ' : 'none', 'Ыы' : '[ɨ]', 'Ьь' : '/ ʲ/', 'Ээ' : '/e/', 'Юю' : '/ju/ or / ʲu/', 'Яя' : '/ja/ or / ʲa/'}
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
hard_indicating_vowel = ['а', 'о', 'э', 'ы', 'у']
soft_indicating_vowel = ['я', 'е', 'ё', 'и', 'ю']
paired_voiced_consonants = ['б', 'в', 'г', 'д', 'ж', 'з']
paired_unvoiced_consonants = ['п', 'ф', 'к', 'т', 'ш', 'с']
unpaired_voiced_consonants = ['л', 'м', 'н', 'р']
unpaired_unvoiced_consonats = ['х', 'ц', 'ч', 'щ']



def alphabet_pronounciation_quiz():
    print('----------------------------------------------')
    print("I will give you a kiril alphabet, speak out what you thought and check the answer by pushing any key")
    print("If you want to stop, input 'stop' after I gave you a question")
    overlap_check = input("Will you allow duplicated question? press y/n : ")
    print('----------------------------------------------')

    if overlap_check == 'y':
        point = 0
        tries = 0
        end = len(kiril_alphabet) - 1
        while 1:
            kiril_list = list(kiril_alphabet.keys())
            question = kiril_list[random.randint(0, end)]
            print("Guess the pronounciation : " + question)
            _ = input()
            if _ == 'stop':
                break
            print("Answer : " + kiril_alphabet[question])
            score_record = int(input("if you got answer type '1', if not type '0' : "))
            print('----------------------------------------------')
            if score_record:
                point += 1
            tries += 1

        print('number of questions was {} and you got {} points'.format(tries, point))

    if overlap_check == 'n':
        questioned_alphabet_idx_list = []
        point = 0
        tries = 0
        end = len(kiril_alphabet) - 1
        while len(questioned_alphabet_idx_list) < 33:
            kiril_list = list(kiril_alphabet.keys())
            idx = random.randint(0, end)
            if idx in questioned_alphabet_idx_list:
                continue

            questioned_alphabet_idx_list.append(idx)
            question = kiril_list[idx]
            print("Guess the pronounciation : " + question)
            _ = input()
            if _ == 'stop':
                break
            print("Answer : " + kiril_alphabet[question])
            while 1:
                score_record = int(input("if you got answer type '1', if not type '0' : "))
                print('----------------------------------------------')
                if score_record == 1:
                    point += 1
                    break
                elif score_record == 0:
                    tries += 1
                    break
                else:
                    print("You pressed wrong key. Please input correct command")
                    _ = input('Press any key to retry')

        print('number of questions was {} and you got {} points'.format(tries, point))

    return 0

def analyze_consonants_sounds(word):
    wordlen = len(word)
    hard_consonants_marking_list = []
    soft_consonants_marking_list = []
    voiced_consonants_marking_list = []
    unvoiced_consonants_marking_list = []

    for letter_idx in range(wordlen):
        letter = word[letter_idx]

        if letter in ['ж', 'ц', 'ш']:
            hard_consonants_marking_list.append(letter_idx)
        elif letter in ['й', 'ч', 'щ']:
            soft_consonants_marking_list.append(letter_idx)
        elif letter_idx != wordlen - 1:
            if letter in consonants:
                if word[letter_idx + 1] in hard_indicating_vowel:
                    hard_consonants_marking_list.append(letter_idx)
                if word[letter_idx + 1] in soft_indicating_vowel:
                    soft_consonants_marking_list.append(letter_idx)
        else:
            if letter in consonants:
                hard_consonants_marking_list.append(letter_idx)

        if letter in unpaired_voiced_consonants or letter in paired_voiced_consonants:
            if letter_idx == wordlen - 1:
                unvoiced_consonants_marking_list.append(letter_idx)
            elif letter in paired_voiced_consonants and (word[letter_idx + 1] in paired_unvoiced_consonants or word[letter_idx + 1] in unpaired_unvoiced_consonats):
                unvoiced_consonants_marking_list.append(letter_idx)
            else:
                voiced_consonants_marking_list.append(letter_idx)
        elif letter in unpaired_unvoiced_consonats or letter in paired_unvoiced_consonants:
            unvoiced_consonants_marking_list.append(letter_idx)

    print('hard and soft : ', end='')
    for letter_idx in range(wordlen):
        letter = word[letter_idx]
        if letter_idx in hard_consonants_marking_list:
            print(Fore.RED + letter + Style.RESET_ALL, end='')
        elif letter_idx in soft_consonants_marking_list:
            print(Fore.BLUE + letter + Style.RESET_ALL, end='')
        else:
            print(letter, end='')

    print('\nvoiced and unvoiced : ', end='')
    for letter_idx in range(wordlen):
        letter = word[letter_idx]
        if letter_idx in voiced_consonants_marking_list:
            print(Fore.RED + letter + Style.RESET_ALL, end='')
        elif letter_idx in unvoiced_consonants_marking_list:
            print(Fore.BLUE + letter + Style.RESET_ALL, end='')
        else:
            print(letter, end='')

    print(' [', end='')
    for letter_idx in range(wordlen):
        letter = word[letter_idx]
        change_key = 0
        if letter in paired_voiced_consonants and letter_idx in unvoiced_consonants_marking_list:
            for i in range(6):
                if paired_voiced_consonants[i] == letter:
                    change_key = i
                    print(paired_unvoiced_consonants[i], end='')
        else:
            print(letter, end='')
    print(']')

    return 0

def consonants_hard_soft_sounds_quiz(voca_dict):
    word_list = list(voca_dict.keys())
    asked_list = []
    max_idx = len(voca_dict) - 1
    print('----------------------------------------------')
    print("I will give you a word, figure out which consonants sounds hard and which consonants sounds soft.")
    print("Then think about why it sounds like that and check the answer by pushing any key")
    print("If you want to stop, input 'stop' after I gave you a question")
    print("The word asked once will not be asked twice.")
    print('hard , voiced = ' + Fore.RED + 'LETTER' + Style.RESET_ALL)
    print('soft , unvoiced = ' + Fore.BLUE + 'LETTER' + Style.RESET_ALL)
    print('----------------------------------------------')

    point = 0
    tries = 0

    while 1:
        idx = random.randint(0, max_idx)
        if idx in asked_list:
            continue
        word = word_list[idx]
        print("Guess the pronounciation : {}".format(word))
        _ = input()
        if _ == 'stop':
            break
        print("Answer : ")
        analyze_consonants_sounds(word)
        while 1:
            score_record = int(input("if you got answer type '1', if not type '0' : "))
            print('----------------------------------------------')
            if score_record == 1:
                point += 1
                break
            elif score_record == 0:
                tries += 1
                break
            else:
                print("You pressed wrong key. Please input correct command")
                _ = input('Press any key to retry')

    print('number of questions was {} and you got {} points'.format(tries, point))
    print('----------------------------------------------')
    return 0

def consonants_sounds_guess():
    print('----------------------------------------------')
    print("Write down the noun. I will figure out how it's consonants pronounced. if you want to quit, type stop")
    print("The guess is only figured out by the database, so please search it on the internet. It could be wrong")
    print('hard , voiced = ' + Fore.RED + 'LETTER' + Style.RESET_ALL)
    print('soft , unvoiced = ' + Fore.Blue + 'LETTER' + Style.RESET_ALL)

    while 1:
        word = input("Write down the noun : ")
        if word == 'stop':
            print('----------------------------------------------')
            break
        else:
            _ = input()
            analyze_consonants_sounds(word)
            print('----------------------------------------------')

    return 0

def pronounciation_review(voca_dict):
    print('----------------------------------------------')
    print("Let's review the pronounciation part.")
    while 1:
        print('select the course and press enter to start')
        print("0 = alphabet pronounciation quiz")
        print("1 = consonants sounds quiz")
        print("2 = consonants sounds guess")
        print("quit = exit")
        select = input()
        if select == '0':
            alphabet_pronounciation_quiz()
        elif select == '1':
            consonants_hard_soft_sounds_quiz(voca_dict)
        elif select == '2':
            consonants_sounds_guess()
        elif select == 'quit':
            _ = input('Are you done? y/n : ')
            if _ == 'y':
                break
        else:
            print("You pressed wrong key. Please input correct command")
            _ = input('Press any key to retry')

    return 0