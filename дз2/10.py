#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть

coin = int(input('Введите количество монет: '))
print(coin)
orel = reshka = 0
for i in range(coin):
    n  = int(input('Орёл(0) или Решка(1): '))
    if n == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f'Переверните {orel} монет на решку, так как их меньше')
elif orel == reshka:
    print(f'Кол-во орлов и решек одинаково, по {orel} штук')
else:
    print(f'Переверните {reshka} монет на орла, их меньше всего')
