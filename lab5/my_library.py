def task5_1(word1, word2):
    '''
    Даны два слова (первое длиннее второго). Заменить во втором слове
    соответствующее количество символов на первое слово.

    :param word1: первое слово
    :param word2: второе слово
    :return result:
    '''

    length_word1 = len(word1)
    length_word2 = len(word2)

    result = word1[0:length_word1 - length_word2] + word2

    return result


def task5_2(text):
    '''
    Дан текст из слов, разделенных знаками препинания. Получить список слов
    текста, у которых первая и последняя буквы совпадают. Каждое слово
    выводит один раз (независимо от количества вхождений)

    :param text: вводимый текст
    :return unique_words: список уникальных слов
    '''
    words = text.replace(',', ' ').replace('.', ' ').split()

    unique_words = []

    for word in words:
        if word[0].lower() == word[-1].lower():
            if word not in unique_words:
                unique_words.append(word)

    return unique_words


def task5_3(text):
    '''
    Дана строка символов, состоящая из произвольного текста, слова разделены
    пробелами. Вывести на экран порядковый номер слова максимальной длины
    и номер позиции строки с которой оно начинается.

    :param text: вводимый текст
    :return max_index, max_position: порядковый номер слова, позиция, с которой оно начинается
    '''
    words = text.split()

    max_length = 0
    max_index = -1
    max_position = -1

    for index, word in enumerate(words): # enumerate позволяет одновременно перебирать и получать индекс каждого элемента

        if len(word) > max_length:
            max_length = len(word)
            max_index = index + 1
            max_position = text.find(word)

    return max_index, max_position


def task5_4(words):
    '''
    В тексте нет слов, начинающихся одинаковыми буквами. Напечатать слова
    текста в таком порядке, чтобы последняя буква каждого слова совпадала с
    первой буквой последующего слова. Если все слова нельзя напечатать в
    таком порядке, найти такую цепочку, состоящую из наибольшего количества слов.

    :param words: вводимые слова
    :return long: длинная цепочка
    '''
    words = words.split()

    long = []                                                       # Переменная для хранения самой длинной цепочки

    # Проверяем каждое слово как начальное
    for start_word in words:
        current_chain = [start_word]                                # Начинаем новую цепочку
        used_words = {start_word}                                   # Множество для отслеживания использованных слов

        # Ищем цепочку
        while True:
            last_letter = current_chain[-1][-1]                     # Последняя буква текущего слова
            found_next = False                                      # Флаг для отслеживания, найдено ли следующее слово

            for word in words:
                if word not in used_words and word[0] == last_letter:
                    current_chain.append(word)                      # Добавляем слово в цепочку
                    used_words.add(word)                            # Помечаем слово как использованное
                    found_next = True                               # Устанавливаем флаг, что слово найдено
                    break                                           # Выходим из цикла, так как нашли следующее слово

            if not found_next:
                break                                               # Если не нашли следующее слово, выходим из цикла

        # Проверяем, является ли текущая цепочка самой длинной
        if len(current_chain) > len(long):
            long = current_chain                                    # Обновляем самую длинную цепочку

    return long


def task5_5(string):
    '''
    Написать регулярное выражение, определяющее является ли данная строка
    GUID с или без скобок. Где GUID это строчка, состоящая из 8, 4, 4, 4, 12
    шестнадцатеричных цифр, разделенных тире.
    – пример правильных выражений: e02fd0e4-00fd-090A-ca30-0d00a0038ba0.
    – пример неправильных выражений: e02fd0e400fd090Aca300d00a0038ba0.

    :param string: вводимая строка
    :return: None
    '''
    import re

    guid_pattern = r'^\{?([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})\}?$'

    if re.match(guid_pattern, string):
        print("Строка корректна.")
    else:
        print("Строка не корректна")



def task5_6(string):
    '''
    Строки, содержащие «cat» в качестве подстроки, игнорируйте регистр.
    Пример строк, которые подходят: «cat», «cat and cat», «Cat»,
    «theCATisHERE». Пример строк, которые не подходят: «kat», «», «cot

    :param string: вводимая строка
    :return: None
    '''
    import re

    pattern = re.compile(r'cat', re.IGNORECASE)    # compile - компилирует в объект, который можно использовать для поиска в строке
                                                          #IGNORECASE - игнорирует регистр

    if pattern.search(string):
        print(f'Подходит: "{string}"')
    else:
        print(f'Не подходит: "{string}"')


def task5_7(text):
    '''
    Заменить все вхождения слова «human» на слово «computer». Запрещается
    использовать обратные ссылки. Указание: используйте «\b». Примеры замен:
    «I need to understand the human mind» → «I need to understand the computer mind»

    :param text: вводимый текст
    :return result: результат
    '''
    import re

    result = re.sub(r'\bhuman\b', 'computer', text, flags=re.IGNORECASE)
    return result
