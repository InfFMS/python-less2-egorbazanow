n = int(input())
k = n %10
if (n>4) and n<21:
    print(n,'лет')
else:
    if k == 1:
            print(n, 'год')
    elif k<5:
            print(n, 'года')
    else:
            print(n, 'лет')