hard_consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ш']
plural_exceptions = []
def make_plural_noun(word):

    if word[-1] in hard_consonants:
        print('plural form : ' + word + 'ы')
        print('Because it ends with hard consonants')
    elif word[-1] == 'a':
        print('plural form : ' + word[:-1:] + 'ы')
        print('Because it ends with a')

    elif word[-1] == 'я':
        print('plural form : ' + word[:-1:] + 'и')
        print('Because it ends with я')
    elif word[-1] == 'ь' or word[-1] == 'й':
        print('plural form : ' + word + 'и')
        if word[-1] == 'ь':
            print('Because it ends with ь')
        else:
            print('Because it ends with и')

    elif word[-1] == 'o':
        print('plural form : ' + word[:-1:] + 'a')
        print('Because it ends with o')
    elif word[-1] == 'e':
        print('plural form : ' + word[:-1:] + 'я')
        print('Because it ends with e')

    elif word in plural_exceptions:
        print('plural form : ' + word + 'и')
        print('Because it is exception')

    return 0

make_plural_noun('кровать')

