n = int(input())
if (n == 1) or ((n%10) == 1):
    print(n, 'год')
elif ((n>1) and (n<5)) or (((n%10)>1)) and ((n%10)<5):
    print(n, 'года')
else:
    print(n, 'лет')
