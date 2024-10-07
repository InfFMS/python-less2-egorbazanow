a = int(input('Введите номер столбца 1 клетки '))
b = int(input('Введите номер строки 1 клетки '))
c = int(input('Введите номер столбца 2 клетки '))
d = int(input('Введите номер строки 1 клетки '))
if (abs(a-c) == abs(b-d)) or (abs(a-c) == 0) or (abs(b-d)==0):
    print('Yes')
else:
    print('NO')