import random

consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
feminine_nouns = []
masculine_nouns = []
neutral_nouns = []
feminine_nouns_ends_with_soft_sign = []
gender_exception = {}

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


def update_noun_gender_list(grammatical_vocabulary_book):

    global feminine_nouns
    global masculine_nouns
    global neutral_nouns
    global feminine_nouns_ends_with_soft_sign

    feminine_nouns = (grammatical_vocabulary_book['feminine_nouns'].keys())
    masculine_nouns = (grammatical_vocabulary_book['masculine_nouns'].keys())
    neutral_nouns = (grammatical_vocabulary_book['neutral_nouns'].keys())
    feminine_nouns_ends_with_soft_sign = (grammatical_vocabulary_book['feminine_nouns_ends_with_soft_sign'].keys())
    gender_exception.update(grammatical_vocabulary_book[gender_exception])

    return 0


def analyze_noun_gender(word):


    word = make_all_letter_small(word)

    if word in feminine_nouns:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
    elif word in masculine_nouns:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a masculine noun(Мужской род)')
    elif word in neutral_nouns:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a neutral noun(Средний род)')
    elif word[-1] in consonants:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a masculine noun(Мужской род)')
        print("Because it ends with 'consonants letter'")
    if word[-1] == 'а' or word[-1] == 'я':
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
        if word[-1] == 'а':
            print("Because it ends with 'a'")
        else:
            print("Because it ends with 'я'")
    elif word[-1] == 'о' or word[-1] == 'е':
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a neutral noun(Средний род)')
        if word[-1] == 'о':
            print("Because it ends with 'o'")
        else:
            print("Because it ends with 'e'")
    elif word[-1] == 'ь':
        if word[:-2] in feminine_nouns_ends_with_soft_sign:
            print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
            print("Because it is ends with '{}'".format(word[:-2]))
        elif word[:-3] == 'сть':
            print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
            print("Because it is ends with 'сть'")

        if word[-4:] == 'тель':
            print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
            print("Because it is ends with 'тeль'")
        elif word[-3:] == 'арь':
            print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
            print("Because it is ends with 'apь'")

    return 0


def noun_gender_quiz(voca_dict):

    word_list = list(voca_dict.keys())
    asked_list = []
    max_idx = len(voca_dict) - 1
    print(max_idx)
    print('----------------------------------------------')
    print("I will give you a word. Answer if it is feminine or masuculine or neutral and why it is.")
    print("The word asked once will not be asked twice.\nif you want to stop, please type 'stop'")
    point = 0
    tries = 0

    while 1:
        idx = random.randint(0, max_idx)
        if idx in asked_list:
            continue
        word = word_list[idx]
        print("Guess the gender : {}".format(word))
        _ = input()
        if _ == 'stop':
            break
        print("Answer : ")
        analyze_noun_gender(word)
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


def noun_gender_guess():

    print('----------------------------------------------')
    print("Write down the noun. I will figure out it's gender. if you want to quit, type stop")
    print("The guess is only figured out by the database, so please search it on the internet. It could be wrong")

    while 1:

        word = input("Write down the noun : ")
        word = make_all_letter_small(word)

        if word == 'stop':
            print('----------------------------------------------')
            break
        else:
            _ = input()
            analyze_noun_gender(word)
            print('----------------------------------------------')

    return 0


def gender_review(selected_voca, grammatical_vocabulary_book):


    voca_dict = selected_voca.update(grammatical_vocabulary_book)
    update_noun_gender_list(grammatical_vocabulary_book)

    print('----------------------------------------------')
    print("Let's review the gender part.")
    while 1:
        print('select the course and press enter to start')
        print("0 = noun gender quiz")
        print("1 = noun gender guess")
        print("quit = exit")
        select = input()
        if select == '0':
            noun_gender_quiz(voca_dict)
        elif select == '1':
            noun_gender_guess()
        elif select == 'quit':
            _ = input('Are you done? y/n : ')
            if _ == 'y':
                break
        else:
            print("You pressed wrong key. Please input correct command")
            _ = input('Press any key to retry')

    return 0