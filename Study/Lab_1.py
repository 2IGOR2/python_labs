#Вариант 23


def read_positive(prompt, allow_zero = False):
    while True:
        try:
            value = float(input(prompt).replace(",","."))
            if value > 0 or (allow_zero and value == 0):
                return value
            print("Ошибка: число должно быть положительным")
        except ValueError:
            print("Ошибка: введите число")


def main():
    n = int(read_positive("Количество дисков: "))

    disks = []

    for i in range(1, n + 1):
        print(f"\nДиск {i}: ")
        total = read_positive(" Общий объем: ")

        while True:
            used = read_positive(" Занятый объем ", allow_zero=True)
            if used <= total:
                break
            print("Ошибка: занятый объем не может превышать общий")
        disks.append((i, total, used, used/total * 100))

    print("\nПроцент заполнения дисков: ")
    for num, total, used, percent in disks:
        print(f" Диск {num}: {percent: .2f}%")

    fullest = max(disks, key=lambda d:d[3])
    print(f"\nНаиболее заполненный диск: №{fullest[0]} ({fullest[3]: .2f}%)")

    avg = sum(d[3] for d in disks) / len(disks)
    print(f"\nСредний процент заполнения: {avg:.2f}%")

    over_90 = sum(1 for d in disks if d[3] > 90)
    print(f"Дисков с заполнением более 90%: {over_90}")

    free = sum(d[1] - d[2] for d in disks)
    print(f"Общий свободный объем: {free:.2f}")

if __name__ == "__main__":
    main()