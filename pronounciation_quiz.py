kiril_alphabet_one = {'Аа' : '/a/', 'Бб' : '/b/', 'Вв' : '/v/', 'Гг' : '/ɡ/', 'Дд' : '/d/', 'Ее' : '/je/', 'Ёё': '/jo/', 'Жж' : '/ʐ/', 'Зз' : '/z/', 'Ии' : '/i/, / ʲi/, or /ɨ/' , 'Йй' : '/j/', 'Кк' : '/k/ or /kʲ/'}
kiril_alphabet_two = {'Лл' : '/ɫ/ or /lʲ/', 'Мм' : '/m/ or /mʲ/', 'Нн' : '/n/ or /nʲ/', 'Оо' : '/o/', 'Пп' : '/p/ or /pʲ/', 'Рр' : '/r/ or /rʲ/', 'Сс' : '/s/ or /sʲ/', 'Тт' : '/t/ or /tʲ/', 'Уу' : '/u/'}
kiril_alphabet_three = {'Фф' : '/f/ or /fʲ/', 'Хх' : '/x/ or /xʲ/', 'Цц' : '/ts/', 'Чч' : '/tɕ/', 'Шш' : '/ʂ/', 'Щщ' : '/ɕː/, /ɕ/', 'Ъъ' : 'none', 'Ыы' : '[ɨ]', 'Ьь' : '/ ʲ/', 'Ээ' : '/e/', 'Юю' : '/ju/ or / ʲu/', 'Яя' : '/ja/ or / ʲa/'}
alphabet_list = kiril_alphabet_one + kiril_alphabet_two + kiril_alphabet_three
hard_indicating_vowel = ['Аа', 'Оо', 'Ээ', 'Ыы', 'Уу']
soft_indicating_vowel = ['Яя', 'Ее', 'Ёё', 'Ии', 'Юю']
paired_voiced_and_unvoiced_consonants = {'Б' : 'П', 'В' : 'Ф', 'Г' : 'К', 'Д' : 'Т', 'Ж' :'Ш', 'З' : 'С'}
paired_unvoiced_and_voiced_consonants = {v : k for k, v in paired_voiced_and_unvoiced_consonants.items()}
unpaired_voiced_consonants = ['Л', 'М', 'Н', 'Р']
unpaired_unvoiced_consonats = ['X', 'Ц', 'Ч', 'Щ']

def alphabet_pronounciation_quiz():