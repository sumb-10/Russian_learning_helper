import random

kiril_alphabet = {'Аа' : '/a/', 'Бб' : '/b/', 'Вв' : '/v/', 'Гг' : '/ɡ/', 'Дд' : '/d/', 'Ее' : '/je/', 'Ёё': '/jo/', 'Жж' : '/ʐ/', 'Зз' : '/z/', 'Ии' : '/i/, / ʲi/, or /ɨ/' , 'Йй' : '/j/', 'Кк' : '/k/ or /kʲ/', 'Лл' : '/ɫ/ or /lʲ/', 'Мм' : '/m/ or /mʲ/', 'Нн' : '/n/ or /nʲ/', 'Оо' : '/o/', 'Пп' : '/p/ or /pʲ/', 'Рр' : '/r/ or /rʲ/', 'Сс' : '/s/ or /sʲ/', 'Тт' : '/t/ or /tʲ/', 'Уу' : '/u/', 'Фф' : '/f/ or /fʲ/', 'Хх' : '/x/ or /xʲ/', 'Цц' : '/ts/', 'Чч' : '/tɕ/', 'Шш' : '/ʂ/', 'Щщ' : '/ɕː/, /ɕ/', 'Ъъ' : 'none', 'Ыы' : '[ɨ]', 'Ьь' : '/ ʲ/', 'Ээ' : '/e/', 'Юю' : '/ju/ or / ʲu/', 'Яя' : '/ja/ or / ʲa/'}
hard_indicating_vowel = ['Аа', 'Оо', 'Ээ', 'Ыы', 'Уу']
soft_indicating_vowel = ['Яя', 'Ее', 'Ёё', 'Ии', 'Юю']
paired_voiced_and_unvoiced_consonants = {'Б' : 'П', 'В' : 'Ф', 'Г' : 'К', 'Д' : 'Т', 'Ж' :'Ш', 'З' : 'С'}
paired_unvoiced_and_voiced_consonants = {v : k for k, v in paired_voiced_and_unvoiced_consonants.items()}
unpaired_voiced_consonants = ['Л', 'М', 'Н', 'Р']
unpaired_unvoiced_consonats = ['X', 'Ц', 'Ч', 'Щ']


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
            score_record = int(input("if you got answer type '1', if not type '0' : "))
            print('----------------------------------------------')
            if score_record:
                point += 1
            tries += 1

        print('number of questions was {} and you got {} points'.format(tries, point))

    return 0


