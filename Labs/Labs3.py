list = [1,2,3,4,5,6,7,8,9,10]
print(list)

from math import fsum
print("Сумма элементов списка: ",str(fsum(list)))

from statistics import mean, median, stdev
print("Среднее значение списка: ",str(mean(list)))
print("Медианное значение списка: ",str(median(list)))
print("Стандартное отклонение списка: ",str(stdev(list)))

from random import randint
print("Случайное число: ",randint(1, 100))