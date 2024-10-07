a_1 = int(input('Начало первого отрезка '))
a_2 = int(input('Конец первого отрезка '))
b_1 = int(input('Начало второго отрезка '))
b_2 = int(input('Конец второго отрезка '))
if a_2 > b_1 and a_2<b_2:
    print(b_1, a_2)
elif a_2 == b_1:
    print(a_2)
else:
    print('Пустое множество')