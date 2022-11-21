# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

# Для двух игроков:
from random import randint

def inputCandies(name):
    number =int(input(f"{name}, введите количество конфет (от 1 до 28): "))
    while number < 1 or number > 28:
        number =int(input(f"{name}, введите количество конфет (от 1 до 28): "))
    return number

def game(candies, queue):    
    if queue: 
        candies=candies-inputCandies('player1')
        queue = 0
    else:
        candies=candies-inputCandies('player2')
        queue = 1
    return candies, queue

queue =randint(0,2)
candies =2021
while (candies>0):
    candies, queue=game(candies, queue)
    print(f'Осталось {candies} конфет')

if queue:
    print ('Выиграл player2')
else:
    print ('Выиграл player1')
