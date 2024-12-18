"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from lab5.my_library import task5_1, task5_2, task5_3, task5_4, task5_5, task5_6, task5_7


def menu():
    """
    Функция предлагает выбор номера задания\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
    """

    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()

        match choice:

            case 1:
                word1 = input("Введите первое слово: ")
                word2 = input("Введите второе слово: ")

                print(f'Результат: {task5_1(word1, word2)}')

            case 2:
                text = input('Введите текст: ')

                print(task5_2(text))

            case 3:
                text = input("Введите строку: ")
                word_index, position = task5_3(text)

                print(f"Порядковый номер слова максимальной длины: {word_index}")
                print(f"Позиция в строке, с которой оно начинается: {position}")

            case 4:
                words = input('Введите слова через пробел: ')

                print(task5_4(words))

            case 5:
                string = input("Введите строку для проверки: ")

                task5_5(string)

            case 6:
                string = input('Введите строку: ')

                task5_6(string)

            case 7:
                text = input("Введите текст: ")
                print(task5_7(text))

            case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

