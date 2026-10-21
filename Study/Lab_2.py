#Вариант 23


NAME, CATEGORY, PRICE, QUANTITY, MANUFACTURER = 0,1,2,3,4

def read_positive(prompt, allow_zero = False):
    while True:
        try:
            value = float(input(prompt).replace(",","."))
            if value > 0 or (allow_zero and value == 0):
                return value
            print("Ошибка: число должно быть положительным")
        except ValueError:
            print("Ошибка: введите число")


def print_medication(medication):
    if len(medication) == 0:
        print("Ничего не найдено")
        return
    print(f"{'Название': <20} {'Категория': <18} {'Цена': >9} {'Количество': >8} Производитель")

    for i in medication:
        print(f"{i[NAME]: <20} {i[CATEGORY]: <18} {i[PRICE]: >9.2f} {i[QUANTITY]: >8} {i[MANUFACTURER]}")


def find_by_manufacturer(medication, manufacturer):
    result = []
    for i in medication:
        if i[MANUFACTURER].lower() == manufacturer.lower():
            result.append(i)
    return result


def filter_by_category(medication, category):
    result = []
    for i in medication:
        if i[CATEGORY].lower() == category.lower():
            result.append(i)
    return result

def total_stock_cost(medication):
    total = 0
    for q in medication:
        total += q[PRICE] * q[QUANTITY]
    return total

def most_expansive(medication):
    if len(medication) == 0:
        return None
    max_price = medication[0]
    for i in medication:
        if i[PRICE] > max_price[PRICE]:
            max_price = i
    return max_price

def manufacturer_list(medication):
    result = []
    for i in medication:
        if i[MANUFACTURER] not in result:
            result.append(i[MANUFACTURER])
    result.sort
    return result

def sort_by_price(medication, descending = False):
    return sorted(medication, key = lambda i: i[PRICE], reverse=descending)


def main():
    medication = [["Парацетамол", "Жаропонижающее", 85, 50, "Фармстандарт"], ["Цитрамон", "Обезболивающее", 60, 40, "Фармстанарт"], 
                  ["Нурофен", "Жаропонижающее", 90, 120, "Reckitt"], ["Аспирин", "Обезболивающее", 70, 150, "Bayer"]]

    menu = "1.Показать все препараты; 2.Поиск препарата по производителю; 3.Фильтр категории; 4.Общая стоимость запасов; 5.Самый дорогой препарат; 6.Список производителей; 7.Сорировка по цене; 0.Выход"


    while True:
        print(menu)
        choice = input("Выберите пункт: ")

        if choice == '1':
            print_medication(medication)
        elif choice == '2':
            print_medication(find_by_manufacturer(medication, input("Производитель:")))
        elif choice == '3':
            print_medication(filter_by_category(medication,input("Категория:")))
        elif choice == '4':
            total_stock_cost(f"Общая стоимость запасов: {total_stock_cost(medication): .2f}")
        elif choice == '5':
            medication = most_expansive(medication)
            print("Самый дорогой препарат: ")
            print_medication([medication])
        elif choice == '6':
            print("Производители:")
            for b in manufacturer_list(medication):
                print('',b)
        elif choice == '7':
            print_medication(sort_by_price(medication))
        elif choice == '0':
            break
        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()