'''
from random import randint
x = []
i = 0
while len(x) != 20:
    i = randint(-20, 20)#числа подбираются случайным образом в диапозоне от 0 до 20
    if i not in x:  #функция используется для исключения возможности повторений
        x.append(i)
print(x)
'''
mas = [['1001001'], ['0101010'], ['0011100'], ['1111111'],

       ['0011100'], ['0101010'], ['1001001']]
for i in range(len(mas)):   #цикл перебирает номер строки
    for j in range(len(mas[i])): #цикл который перебирает элементы строки
        print(mas[i][j], end=' ') 
    print()
