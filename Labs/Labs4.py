#Работа с оператором ветвления
from random import randint
import time

igrok1 = input('Введите имя 1-го играющего: ')
igrok2 = input('Введите имя 2-го играющего: ')

print('Кубик бросает', igrok1)
time.sleep(2)
n1 = randint(1, 6)
print('Выпало:', n1)

print('Кубик бросает', igrok2)
time.sleep(2)
n2 = randint(1, 6)
print('Выпало:', n2)

if n1 > n2:
    print('Выиграл(а)', igrok1)
elif n1 < n2:
    print('Выиграл(а)', igrok2)
else:
    print('Ничья')

#Использование циклов
print("\nНачало партии")
playerPoints = {"playerOne":0,"playerTwo":0}

for throw in range(5) : 
    print('Кубик бросает', igrok1)
    time.sleep(2)
    n1 = randint(1, 6)
    print('Выпало:', n1)
    playerPoints["playerOne"] += n1

    print('Кубик бросает', igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало:', n2)
    playerPoints["playerTwo"] += n2

if playerPoints["playerOne"] > playerPoints["playerTwo"] :
    print('Выиграл(а)', igrok1)
elif playerPoints["playerOne"] < playerPoints["playerTwo"] :
    print('Выиграл(а)', igrok2)
else:
    print('Ничья')
    