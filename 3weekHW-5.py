from functools import reduce

def my_list(el1, el2):
    return el1 * el2

my_list_2 = [el for el in range(100, 1001) if el %2 == 0] #удобнее использовать шаг


print(f'list\n{my_list_2}\nmulti[plication of num\n{reduce(my_list, my_list_2)}')
