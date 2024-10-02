n = int(input())
if ((n <= 2) or (n == 12)) and n!=0:
    print('Зима')
elif (n > 2) and (n <= 5):
    print('Весна')
elif (n>5) and (n <=8):
    print('Лето')
elif (n>8) and (n <= 11):
    print('Осень')
else:
    print('Неверно набранный месяц')