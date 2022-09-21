# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open('incoming_text.txt','w') as file:
#     file.write(input('Введите первоночальный текст: '))
# with open('incoming_text.txt','r') as file:
#     my_text = file.readline()
#     change_text = my_text.split()
# del_text = input('Введите  набор букв, который нужно удалить:  ')
# result = ' '.join(filter(lambda x: del_text not in x, change_text))
# with open('format_text.txt','w') as file:
#     file.write(f'{result}')
# print(result)

# Задача 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: 
# На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного
#  или больше чем имеется в куче.

# b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать 29 конфет, 
# то он, однозначно, проиграет. Достаточно довести игру до такой ситуации.
# **********************
# Человек против человека
# from random import randint

# candies = int(input('Введите общее количество конфет в игре: '))
# gamer1 = input('Введите имя первого игрока: ')
# gamer2 = input('Введите имя второго игрока: ')
# flag = randint(0, 2)
# if flag:
#     print(f'Первый ход у {gamer1}')
# else:
#     print(f'Первый ход у {gamer2}')

# def step_check(name):
#     number = int(input(f'{name}, введите количество конфет в диапазоне от 1 до 28: '))
#     if 1 <= number <= 28:
#         return number
#     else:
#         number = int(input("Необходимо взять конфеты в диапазоне от 1 до 28 шт.: "))
#         return number

# def step_print(name, numb, candy):
#     print(f'{name} взял {numb} конфет. В куче осталось {candy} конфет')


# while candies > 0:
#     if flag:
#         num = step_check(gamer1)
#         candies -= num
#         flag = False
#         step_print(gamer1, num, candies)
#     else:
#         num = step_check(gamer2)
#         candies -= num
#         flag = True
#         step_print(gamer2, num, candies)
# if flag:
#     print(f'Выиграл {gamer2}')
# else:
#     print(f'Выиграл {gamer1}')


#a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного или больше чем имеется в куче.
# from random import randint

# вариант человека против бота:
#
# from random import randint

# candies = 2021
# print(f'Игра против бота, на столе {candies} конфет.Выигрывает тот,кто забирает последние конфеты')
# step = randint(0, 2)
# while candies > 0:
#     if step:
#         if candies > 28:
#             bot = randint(0, 29)
#         else:
#             bot = randint(0, candies)
#         candies -= bot
#         print(f'Бот взял {bot} конфет, на столе осталось {candies}')
#         step = False
#     else:
#         people = int(input('Сколько конфет берёте от 1 до 28? \n'))
#         if 1 <= people <= 28:
#             candies -= people
#             print(f'На столе осталось {candies} конфет')
#             step = True
#         else:
#             people = int(input('Введите количество от 1 до 28: '))
# if step:
#     print('Вы победили!')
# else:
#     print('Вы проиграли. Победил Бот.')

#*********************************
# вариант игры с интеллектуальным ботом
# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
# def bot_calc(value):
#     k = randint(1,29)
#     while value-k <= 28 and value > 29:
#         k = randint(1,29)
#     return k
# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
# counter1 = 0 
# counter2 = 0
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# 3. Задача Создайте программу для игры в ""Крестики-нолики"".


# print('*'*100)
# print('\n')
# print('Давайте сыграем в крестики нолики!')

# board = list(range(1,10))

# def design_board(board):
#     print('-'*12)
#     for i in range(3):
#         print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
#         print('-'*12)
# def choice(tic_tac):
#     valid = False
#     while not valid:
#         player_index = input('Ваш ход, выберите ячейку ' + tic_tac + ' --> ')
#         try:
#             player_index =int(player_index)
#         except:
#             print('Что то не то нажали')
#             continue
#         if player_index >= 1 and player_index <= 9:
#             if(str(board[player_index-1]) not in 'XO'):
#                 board[player_index-1] = tic_tac
#                 valid = True
#             else:
#                 print('Занято')
#         else:
#             print('Еще раз попробуй')

# def victory_check(board):
#     victory = ((0,1,2),(3,4,5),(6,7,8),
#                (0,3,6),(1,4,7),(2,5,8),
#                (0,4,8),(2,4,6))
#     for i in victory:
#         if board[i[0]] == board[i[1]] == board[i[2]]:
#             return board[i[0]]
#     return False

# def game(board):
#     counter =0
#     vic = False
#     while not vic:
#         design_board(board)
#         if counter % 2 == 0:
#             choice('X')
#         else:
#             choice('0')
#         counter +=1
#         if counter > 4:
#             tt_win = victory_check(board)
#             if tt_win:
#                 print(tt_win,'Победа')
#                 vic = True
#                 break
#             if counter == 9:
#                 print('Победила, ДРУЖБА)')
#         design_board(board)
# game(board)

# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('file_encode.txt', 'w') as data:
    data.write('NNNNbbbHHHHLLLLpppjjhh')
def coding(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res
def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res
with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()
with open('file_decode.txt', 'w') as file:
    encoded_string = coding(decoded_string)
    file.write(encoded_string)

print(f"Текст после кодировки: {coding(decoded_string)}")
print(f"Текст после дешифровки: {decoding(coding(decoded_string))}")
