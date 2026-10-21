#Задание 8

import random
def list_to_dict(n,a = 1,b = 100):
    list = [random.randint(a,b) for i in range(n)]
    return dict((i,x) for i,x in enumerate(list))

print(list_to_dict(4))