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

# def encode_file(my_text):  
#     str_code = ''
#     count = 1       
#     for i in range(len(my_text)):
#         if i < len(my_text)-1:
#             if my_text[i] == my_text[i + 1]:
#                 count += 1
#             else:
#                 str_code += str(count) + my_text[i]
#                 count = 1
#         else:
#             str_code += str(count) + my_text[i]
#     return str_code

# def decode_file(strc):
#     count = ''
#     result = ''
#     for i in strc:
#         if i.isdigit():
#             count += i
#         else:
#             result += i * int(count)
#             count = ''
#     return result

# text = 'MMMMfffGGGHHHHCCCKKKDDDDqqqq'
# print(f'Введён следующий текст: \n{text}')
# with open('5_decode.txt', 'w') as data:
#     data.write(text)

# with open('5_decode.txt', 'r') as data:
#     my_text = data.read()

# strc = encode_file(my_text)
# print(f'Сжатый текст: \n{strc}') 

# with open('5_code2.txt', 'w') as data:
#     data.write(strc)

# with open('5_code2.txt', 'r') as data:
#     my_text = data.read()

# total = decode_file(my_text)
# print(f'Восстановленный текст: \n{total}') 

# with open('5_decode.txt', 'w') as data:
#     data.write(total)