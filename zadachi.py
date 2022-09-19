# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('incoming_text.txt','w') as file:
    file.write(input('Введите первоночальный текст: '))
with open('incoming_text.txt','r') as file:
    my_text = file.readline()
    change_text = my_text.split()
del_text = input('Введите  набор букв, который нужно удалить из слов содержащие данную последовательность :  ')
result = ' '.join(filter(lambda x: del_text not in x, change_text))
with open('format_text.txt','w') as file:
    file.write(f'{result}')
print(result)