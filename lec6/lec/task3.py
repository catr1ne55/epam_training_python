#!/usr/bin/env python3


def division():
    """Вводится число пар, после чего происходит ввод каждой пары(элементы пары вводтся через пробел),
     затем производится деление первого элемента пары на второй элемент. Если по каким-то причинам деление невозможно -
     отображается соответствующее сообщение."""

    pairs = int(input("Введите кол-во пар > "))
    pairs_list = []
    for i in range(pairs):
        pairs_list.append(input())
    for i in range(pairs):
        try:
            a, b = [int(number) for number in pairs_list[i].split(' ')]
            print(a / b)
        except (ValueError, ZeroDivisionError) as e:
            print("Error code: " + e.__str__())


if __name__ == '__main__':
    division()
