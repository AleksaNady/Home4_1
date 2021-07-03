
-----#2 с Преподавателем
from random import randint

mylist = [randint(-10,10) for _ in range(20)]
uniq_list = [el for el in mylist if mylist.count(el)== 1]
print(f"создание списка\n{mylist}\nнепоторяющиеся элементы\n{uniq_list}")

-----#2 по задаче
my_list1 =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniq_list = [el for el in my_list1 if my_list1.count(el)== 1]
print(f"создание списка\n{my_list1}\nнепоторяющиеся элементы\n{uniq_list}")