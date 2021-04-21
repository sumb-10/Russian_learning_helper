consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
feminine_nouns = []
masculine_nouns = []
neutral_nouns = []
feminine_nouns_ends_with_soft_sign = []
masculine_nouns_ends_with_soft_sign = []
gender_exception ={}

def analyze_noun_gender(word):
    wordlen = len(word)

    if word in feminine_nouns:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a feminine noun(Женский род)')
    elif word in masculine_nouns:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a masculine noun(Мужской род)')
    elif word in neutral_nouns:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a neutral noun(Средний род)')
    elif word[-1] in consonants:
        print("\033[34m" + '{} '.format(word) + "\033[0m" + 'is a masculine noun(Мужской род)')
        print("Because it ends with 'consonants letter'")
    elif word[-1] == 'а' or word[-1] == 'я':
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

analyze_noun_gender('Писатель')

