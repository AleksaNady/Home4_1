from itertools import cycle
from itertools import count

my_count = count(3)
my_cycle = cycle("ABC")

for _ in range(10):
    print("(my_count, my_cycle) = ({},{})".format(next(my_count), next(my_cycle)))