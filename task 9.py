a = int(input('Введите номер столбца 1 клетки '))
b = int(input('Введите номер строки 1 клетки '))
c = int(input('Введите номер столбца 2 клетки '))
d = int(input('Введите номер строки 1 клетки '))
if (abs(a-c) == 1) and (abs(b-d) == 2) or (abs(a-c)==2 and (abs(b-d) == 1)):
    print('YES')
else:
    print('NO')