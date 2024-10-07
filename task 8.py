a = int(input('Введите номер столбца 1 клетки '))
b = int(input('Введите номер строки 1 клетки '))
c = int(input('Введите номер столбца 2 клетки '))
d = int(input('Введите номер строки 1 клетки '))
if abs(a - c) == abs(b-d):
    print('Yes')
else:
    print('NO')