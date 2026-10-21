#Задание 8

def Lab1(list):
    for x in list:
        if x == 2 or x == 3:
            return "True"
    return False

print(Lab1([1,5,6,7,8,9,11]))